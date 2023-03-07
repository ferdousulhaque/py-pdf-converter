# This is a sample Dockerfile

# set base image python:3.8-slim-buster
FROM python:3.10-slim

# set working directory as app
WORKDIR /usr/src/app

# copy requirements.txt file from local (source) to file structure of container (destination)
COPY requirements.txt ./

# Install the requirements specified in file using RUN
RUN pip install --no-cache-dir -r requirements.txt

# copy all items in current local directory (source) to current container directory (destination)
COPY . .

# command to run when image is executed inside a container
CMD [ "python", "./main.py" ]