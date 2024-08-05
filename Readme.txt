Flask Application with Blueprint Functionality

Unit Test Cases: To run the unit test cases for the Flask application, use the command:


python3 -m unittest tests/test.py
Run the Flask Application: To start the Flask application, use the command:



python3 run.py
Build Docker Image: To build the Docker image, use the command:

docker build -t python-git .
Run Docker Container: To run the Docker container, use the command:

docker run -p 80:8080 python-git
Deploy in Kubernetes: To deploy the application in Kubernetes, use the command:

helm install pythongit python-git/ --namespace git