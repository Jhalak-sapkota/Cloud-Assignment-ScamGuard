"""Run `python seed.py` to create one demo user per role for quick testing."""
from werkzeug.security import generate_password_hash

from app import create_app
from extensions import db
from models import User

app = create_app()

with app.app_context():
    db.create_all()
    if not User.query.filter_by(email='reporter@test.com').first():
        db.session.add_all([
            User(name='Alice Reporter', email='reporter@test.com',
                 password_hash=generate_password_hash('password123'), role='reporter'),
            User(name='Bob Verifier', email='verifier@test.com',
                 password_hash=generate_password_hash('password123'), role='verifier'),
            User(name='Cara Educator', email='educator@test.com',
                 password_hash=generate_password_hash('password123'), role='educator'),
        ])
        db.session.commit()
        print('Seeded demo users (password for all: password123)')
    else:
        print('Demo users already exist.')
