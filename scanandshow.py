from flask import Flask, render_template, request
import requests as apirequest
app = Flask(__name__)
key=""
weatherkey=""
@app.route('/')
def index():
    f=open("number.txt",'r')
    num=f.readline()
    f.close()
    return render_template('time.html', number=num)
if __name__ == '__main__':
    app.run(
     host="0.0.0.0",
    port=80
 )
    
