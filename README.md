# MS-Email-Send

A lightweight microservice built with FastAPI for asynchronous email sending. Uses Redis and Celery for task queueing and Docker for easy deployment.

## Fast start

1.  `git clone https://github.com/miroslav-fedechkin/MS-email-send`
2.  `cd MS-email-send`
3.  `pip install -r requirements.txt`
4.  Configure the `.env` file (use `env_example` as a reference)
    - *For Gmail SMTP setup: If you don't know how to create an App Password, read [this guide](https://support.google.com/mail/answer/185833?hl=en).*
5.  `docker-compose up`

## Key technologies

- Python 3.12.4
- FastAPI
- Redis & Celery
- Docker
