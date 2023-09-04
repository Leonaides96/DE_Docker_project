## Dockerfile is the area where can configurate and build the image
## 

# set base image (host os)
FROM python

# set the working dir in the container
WORKDIR /code

# copy the dependencies file to the working dir
#COPY source dest
COPY requirements.txt .

# install the dependecies
RUN pip install -r requirements.txt 

# copy the content of the local src dir  to the working dir
COPY src/ .

# Command to run on container start
CMD ["python", "./app_testing.py"]