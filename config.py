from fastapi_mail import ConnectionConfig
import os
from dotenv import load_dotenv

load_dotenv()



conf = ConnectionConfig(
    MAIL_USERNAME = os.getenv('MAIL_USERNAME'),
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD'),
    MAIL_PORT = os.getenv('MAIL_PORT'),
    MAIL_SERVER = os.getenv('MAIL_SERVER'),
    MAIL_SSL_TLS = os.getenv('MAIL_SSL_TLS'),
    MAIL_STARTTLS = os.getenv('MAIL_STARTTLS'),
    MAIL_DEBUG = os.getenv('MAIL_DEBUG'),
    MAIL_FROM = os.getenv('MAIL_FROM'),

)