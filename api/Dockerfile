FROM python:3.12

WORKDIR /app

COPY ./ /app/

# Since pyproject.toml is in /app we can install from there now
RUN pip install .

ENTRYPOINT ["python3", "/app/src/capstone2/main.py"]
# this is how we are running the file and the path to what file we are using to initiate 

# From the same directory as this Dockefile run
# docker build -t capstone2example . && docker run capstone2example