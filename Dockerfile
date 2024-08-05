# Use an official Python runtime as a parent image
FROM python:3.9-slim

WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

RUN  python -m unittest tests/test.py

EXPOSE 8000

ENTRYPOINT [ "python" ] 
CMD [ "run.py" ]
