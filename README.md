# Loch_Technologies_Assignment
 There are 2 main files : client.py and app.py(flask server)
## Usage of client.py

1) The script client.py can be run on the command line using the following command:
   python client.py val1 val2 op (passes two operands and an operator to the function)

2) A call is then made to the flask server which is running inside a docker container which is responsible for verifying the data using ecdsa signature and then performs a simple calculation

## Running the flask server through Docker

Assuming all prerequisities including Docker is installed in your system,the following steps are to be followed: 

1) Clone the repository
2) Dockerfile is already present in the repository which we use to build a docker image
3) Build the dockerfile to create docker image as follows:
     -  docker build --tag name .
4) To check if the image is created do the following:
   - docker images 

   Here you should find that your image is created

5) Next run the image as follows( by default the flask server runs on port 5000, which can be tweaked in the Dockerfile)
    -  docker run -p 5000:5000 -it image_name
6) The flask server has two endpoints at localhost:5000
    1) get_api_key
    2) verify_api_key
