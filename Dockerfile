FROM python:3.11.4-alpine

COPY . .
RUN pip3 install pyTelegramBotAPI
CMD ["python3", "app.py"]
