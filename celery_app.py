import asyncio
from celery import Celery
from fastapi.responses import JSONResponse
from fastapi_mail import FastMail, MessageSchema
from config import conf

celery = Celery(
    'email_worker',
    broker='redis://localhost:6379/0',  
    backend='redis://localhost:6379/0'  
)

@celery.task
def send_email(email):
    print(f"Sending...")
    with open('message_text.html', 'r', encoding='utf-8') as file:
        html_content = file.read()

    message = MessageSchema(
        subject='FastAPI-Mail module',
        recipients=email,
        body=html_content,
        subtype='html'
    )

    

    fm = FastMail(conf)
    try:
        asyncio.run(fm.send_message(message))
        return 'success' 
        
    except Exception as e:
        print(e)