from flask import Flask, render_template, request
import requests as apirequest
app = Flask(__name__)
key=""
weatherkey=""
@app.route('/')
def index():
    ip = request.remote_addr
    r=apirequest.get('https://api.ipgeolocation.io/ipgeo?apiKey={0}&ip={1}&fields=geo'.format(key,ip))
    thedict=r.json()
    try:
        zipcode=thedict['zipcode']
        countrycode=thedict['country_code2']
        wr=apirequest.get('http://api.openweathermap.org/data/2.5/weather?zip={0},{1}&appid={2}'.format(zipcode,countrycode,weatherkey))
        weatherdict=wr.json()        
        weather=weatherdict['weather'][0]['main']
    except Exception:
        return render_template('weather.html', user_weather='Cannot get your location')
    return render_template('weather.html', user_weather=weather,user_loc=thedict['zipcode'])
if __name__ == '__main__':
    app.run(
    host="0.0.0.0",
    port=80
 )
    
