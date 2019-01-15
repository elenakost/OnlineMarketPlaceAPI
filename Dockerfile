FROM python:3.6-slim

WORKDIR /app

# WORKDIR sets the currently working directory and creates it if not exist.
# The below command can be simplified as 
# ADD . .
ADD . .

RUN python3 -m pip install -r requirements.txt

ENV FLASK_DEBUG=1

EXPOSE 80

CMD ["python", "app.py"]
