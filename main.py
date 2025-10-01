from fastapi import FastAPI
from config import conf
from fastapi_mail import FastMail, MessageSchema
from shemas import EmailShema
from starlette.responses import JSONResponse

app = FastAPI()


@app.post('/send_email')
async def send_email(email: EmailShema):

    with open('message_text.html', 'r', encoding='utf-8') as file:
        html_content = file.read()

    message = MessageSchema(
        subject='FastAPI-Mail module',
        recipients=email.model_dump().get('email'),
        body=html_content,
        subtype='html'
    )

    

    fm = FastMail(conf)
    try:
        await fm.send_message(message)
        return JSONResponse(status_code=200, content={
            'status': 'ok'
        })
    except Exception as e:
        print(e)

