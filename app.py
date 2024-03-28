from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<html><body><style>.uno{display:flex;text-aling:center;flex-direction:column}</style><div class="un    o" ><img src="https://img.freepik.com/psd-gratis/ilustracion-3d-avatar-o-perfil-humano_23-2150671142.jpg?size    =338&ext=jpg&ga=GA1.1.1297763733.1711497600&semt=sph"height="200px" width="200px"><h1>ABEL ALAN GARCIA PEREZ<    /h1><p>programador</p></div></body></html>'
   
 
if __name__ == '__main__':
   app.run(debug=True)