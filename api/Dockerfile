# Use an official Python runtime as a parent image
FROM python:3.12

# !adding database
# Update the package list, install postgresql-client, and clean up
# RUN apt-get update && \
#     apt-get install -y postgresql-client && \
#     rm -rf /var/lib/apt/lists/*

# !adding database
# Copy the requirements file into the container
# COPY ./requirements.txt /app/requirements.txt

# Set the working directory in the container to /app
WORKDIR /app

# Install FastAPI + incase
RUN pip install fastapi[all] incase

# Copy main.py
# ! note this might need to be COPY main.py /app/main.py
COPY ./src/capstone2/main.py /app/main.py
# COPY main.py /app/main.py
# COPY ./ /app/

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run uvicorn when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]