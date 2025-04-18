# set base image (host OS)
FROM python:3.9

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY danzer/requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY danzer/anonymizer/core/ .

# command to run on container start
CMD [ "python", "./app.py" ]