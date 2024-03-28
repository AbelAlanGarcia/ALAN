from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<html><body><style>.uno{display:flex;text-aling:center;flex-direction:column}</style><div class="uno" ><img src="https://scontent.fjau2-1.fna.fbcdn.net/v/t39.30808-6/327756228_926342525045166_486223238458086767_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=5f2048&_nc_eui2=AeE3-37IzHhXqFbO9Y4m5-xONW93NcRfJZ01b3c1xF8lnYGf2R0tt4Wf456yGSWplYrMRjmAyWBT79UdocsDxUGl&_nc_ohc=_ZIXm__zF_sAX-JW3hj&_nc_ht=scontent.fjau2-1.fna&oh=00_AfCcxTCdZMYfZ1dB_sQo2A_7vQg760aCvIadPrGpud8X4g&oe=660AC23B"height="200px" width="200px"><h1>ABEL ALAN GARCIA PEREZ</h1><p>JUGADOR CAMISETA 7</p></div></body></html>'
   
 
if __name__ == '__main__':
   app.run(debug=True)
