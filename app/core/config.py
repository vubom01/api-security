import os
import fastapi_mail

from dotenv import load_dotenv
from pydantic import BaseSettings

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
load_dotenv(os.path.join(BASE_DIR, '.env'))


class Settings(BaseSettings):
    API_PREFIX = ''
    PROJECT_NAME = os.getenv('PROJECT_NAME', '')
    LOGGING_CONFIG_FILE = os.path.join(BASE_DIR, 'logging.ini')
    RUNNING_PORT = os.getenv('RUNNING_PORT', '')
    BACKEND_CORS_ORIGINS = ['*']

    DOMAIN = os.getenv('DOMAIN', '')
    API_AUDIENCE = os.getenv('API_AUDIENCE', '')
    ALGORITHMS = os.getenv('ALGORITHMS', '')
    ISSUER = os.getenv('ISSUER', '')

    MYSQL_SERVER = os.getenv('MYSQL_SERVER')
    MYSQL_USER = os.getenv('MYSQL_USER')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
    MYSQL_DB = os.getenv('MYSQL_DB')
    DATABASE_URI = f"mysql+mysqldb://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_SERVER}/{MYSQL_DB}"

    ACCESS_TOKEN_EXPIRE_SECONDS: int = 60 * 60 * 24 * 7  # Token expired after 7 days
    SECRET_KEY = os.getenv('SECRET_KEY', '')
    SECURITY_ALGORITHM = os.getenv('SECURITY_ALGORITHM', '')


settings = Settings()

