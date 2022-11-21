# Version of Python to use
FROM python:3.10

# Set the working directory, ej. /app
WORKDIR /app
# Copying the requirements.txt file from the local directory to the /app directory in the container.
COPY requirements.txt /app/requirements.txt
# Install the dependencies from the requirements.txt file
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
# Copy the current directory to the /app directory in the container.
COPY . /app

# Run the app.py file when the container launches
CMD bash -c "while true; do sleep 1; done"