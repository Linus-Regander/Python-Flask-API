from flask import Flask
from api import api
from config import load_config

def setup_app():
    flask_app = Flask(__name__)
    ctx =  flask_app.app_context()
    ctx.push()
    api.init_app( flask_app)

    return  flask_app

app = setup_app()

if __name__ == '__main__':
    print("loading config...")
    config = load_config()

    print("starting app...")
    app.run(host=config.host, port=config.port, debug=config.debug, load_dotenv=True)