import os
from pathlib import Path

class Config:
    BASE_DIR = Path(__file__).parent
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(BASE_DIR / 'instance' / 'devops.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-123'
    FLASK_ENV = os.environ.get('FLASK_ENV', 'development')
    DEBUG = FLASK_ENV == 'development'