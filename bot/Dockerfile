FROM python:3.9.6-alpine

WORKDIR /conteiner_bot

ENV PYTHONWRITEBYECODE 1
ENV PYTHONBUFFERED 1




COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY * ./

CMD ["python", "bot.py"]