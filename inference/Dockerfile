# Use a lightweight base image
FROM python:3.8-slim

# Install necessary packages
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt


COPY . /app
WORKDIR /app

# Run the entrypoint script
#CMD python /app/app.py
CMD ["/bin/sh", "-c", "gunicorn --bind 0.0.0.0:5000 --workers 1 --timeout 3600 app:app"]
