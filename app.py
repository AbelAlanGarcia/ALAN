from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<html><body><style>.uno{display:flex;text-aling:center;flex-direction:column}</style><div class="uno" ><img src="blob:https://web.whatsapp.com/73c65f08-c362-4090-ba77-6ee2bdf778fa"height="200px" width="200px"><h1>ENANO HDP</h1><p>JUGADOR CAMISETA 7</p></div></body></html>'
   
 
if __name__ == '__main__':
   app.run(debug=True)
