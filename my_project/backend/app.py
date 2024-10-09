from flask import Flask
from database import create_app
from routes import api

app = create_app()
app.register_blueprint(api, url_prefix='/api')

if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True, host='0.0.0.0')
