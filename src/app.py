from flask import Flask

from config import config

#Routes
from routes import movie

app = Flask(__name__)

def page_not_found(error):
    return "<h1> Pagina en blanco </h1>",404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    
    #Blueprints
    app.register_blueprint(movie.main, url_prefix='/api/movies')
    
    #error handlers
    app.register_error_handler(404,page_not_found)
    
    app.run()
