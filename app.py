import os

from flask import Flask

from config import Config
from extensions import db, login_manager
from models import User


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    db.init_app(app)
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from routes.alerts import alerts_bp
    from routes.articles import articles_bp
    from routes.auth import auth_bp
    from routes.reports import reports_bp
    from routes.verify import verify_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(reports_bp)
    app.register_blueprint(verify_bp)
    app.register_blueprint(articles_bp)
    app.register_blueprint(alerts_bp)

    with app.app_context():
        db.create_all()  # convenient for dev/demo; use proper migrations for production

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
