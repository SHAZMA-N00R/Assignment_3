FROM python:3.11

# Copy the requirements file
COPY ./requirements.txt /webapp/requirements.txt

# Set the working directory
WORKDIR /webapp

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the webapp files
COPY webapp/* /webapp

# Define the entry point and command
ENTRYPOINT [ "uvicorn" ]
CMD [ "--host", "0.0.0.0", "main:app" ]
