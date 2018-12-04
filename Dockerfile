FROM python:3.6-alpine
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 80
ENTRYPOINT ["python3", "server.py"]