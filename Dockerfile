# base image is use for building the Docker image. The pypy image is 
# a pre-built image that provides a Python interpreter with a 
# focus on speed and memory efficiency.
FROM pypy:latest
# This instruction sets the working directory within the container to /app.
WORKDIR /app
# This line copies the requirements.txt file from the host 
# (the system where the Docker build command is executed) 
# to the /app directory inside the container. 
COPY requirements.txt /app
# This command runs the pip install command inside the container, 
# installing the Python packages specified in the requirements.txt file. 
# The -r flag tells pip to read the requirements from a file.
RUN pip install -r requirements.txt
# This line copies all the files and directories 
# from the current directory on the host (where the Dockerfile is located) 
# to the /app directory inside the container. 
# It ensures that all the necessary application files are available 
# within the container.
COPY . /app
# This instruction sets the default command 
# to be executed when the container is run. 
# It specifies the command as python watch_next.py,
# it will run the Python script named watch_next.py
# using the Python interpreter installed in the container.
CMD ["python", "watch_next.py"]