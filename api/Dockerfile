FROM python:3.12

# Update the package list, install postgresql-client, and clean up
# ! try this
# RUN apt-get update && \
#     apt-get install -y postgresql-client && \
#     rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ./ /app/
# COPY ./src/capstone2/main.py /app/main.py
# Since pyproject.toml is in /app we can install from there now
# RUN pip install .
RUN pip install fastapi[all] incase

# ENTRYPOINT ["python3", "/app/src/capstone2/main.py"]
# this is how we are running the file and the path to what file we are using to initiate 

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run uvicorn when the container launches
CMD ["uvicorn", "src.capstone2.main:app", "--host", "0.0.0.0", "--port", "8000"]
# because this is a library (check the pyproject.toml you need to have your library folder in src name its a lubrary of of imports? )

# From the same directory as this Dockefile run
# docker build -t capstone2example . && docker run capstone2example