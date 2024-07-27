FROM python:3.12.4-alpine3.20

# We need curl for the health check
RUN apk --no-cache add curl

WORKDIR /app

# first copy depencencies  only
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# copy the app source seprately improve the speed of runing CI/CD pipeline
# Building the app from the cache if non depedencies are added
COPY app.py .

# in production we use often "gunicorn" & all network interfaces and ports
CMD [ "gunicorn", "--bind", "0.0.0.0:8080", "app:app" ]

# pip install gunicorn
# pip freeze -> requirements.txt