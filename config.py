from fastapi_mail import ConnectionConfig
import os
from dotenv import load_dotenv

load_dotenv()



conf = ConnectionConfig(
    MAIL_USERNAME = os.getenv('MAIL_USERNAME'),
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD'),
    MAIL_PORT = os.getenv('MAIL_PORT'),
    MAIL_SERVER = os.getenv('MAIL_SERVER'),
    MAIL_TLS = os.getenv('MAIL_TLS'),
    MAIL_SSL = os.getenv('MAIL_SSL'),
)