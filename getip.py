from flask import Flask, render_template, request
import geoip2.database
reader = geoip2.database.Reader('./GeoLite2-City.mmdb')
app = Flask(__name__)
@app.route('/')
def index():
    ip = request.remote_addr
    
    return render_template('index.html', user_ip=ip)
if __name__ == '__main__':
    app.run(
     host="0.0.0.0",
    port=80
 )