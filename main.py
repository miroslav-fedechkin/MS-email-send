from fastapi import FastAPI
from config import conf
from fastapi_mail import FastMail, MessageSchema
from shemas import EmailShema
from starlette.responses import JSONResponse
from celery_app import send_email

app = FastAPI()


@app.post('/send_email')
async def send(email: EmailShema):
    send_email.delay(email = email.to_email)
    return {'status': 'proccesing..'}
