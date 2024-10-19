from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<html><body><style>.uno{display:flex;text-aling:center;flex-direction:column}</style><div class="uno" ><img src="https://www.fichajes.com/build/images/player-covers/cristiano-ronaldo.352c95f5.jpg"height="200px" width="200px"><h1>ABEL ALAN GARCIA PEREZ</h1><p>JUGADOR CAMISETA 7</p></div></body></html>'
   
 
if __name__ == '__main__':
   app.run(debug=True)
