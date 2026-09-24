import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-change-me')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///local.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    AWS_REGION = os.environ.get('AWS_REGION', 'ap-southeast-1')
    S3_BUCKET = os.environ.get('S3_BUCKET')
    SQS_QUEUE_URL = os.environ.get('SQS_QUEUE_URL')
    SNS_TOPIC_ARN = os.environ.get('SNS_TOPIC_ARN')

    USE_S3 = bool(os.environ.get('S3_BUCKET'))
    USE_SQS = bool(os.environ.get('SQS_QUEUE_URL'))
    USE_SNS = bool(os.environ.get('SNS_TOPIC_ARN'))

    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'uploads')
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5 MB evidence upload cap
