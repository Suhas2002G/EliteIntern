import os
import secrets
from datetime import timedelta
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager


from routes.auth_routes import auth_bp
from routes.admin_routes import admin_bp
from routes.user_routes import user_bp

def create_app():
    frontend_url = os.getenv('FRONTEND_URL')
    app = Flask(__name__)
    CORS(app, supports_credentials=True, origins=[frontend_url])

    secret_key = secrets.token_hex(16)
    app.secret_key = secret_key
    #session will expire after 1 hour of inactivity.
    app.permanent_session_lifetime = timedelta(hours=1)
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", secret_key)
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=480)
    app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=14)
    app.config['JWT_BLACKLIST_ENABLED'] = True
    app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

    # Initialize extensions
    jwt = JWTManager(app)

    # app.config.from_object(Config)

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(admin_bp, url_prefix='/admin')

    return app

# Run the server
if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5050, debug=True)