# use python 3.11 base image
FROM python:3.11

# set the working directory
WORKDIR /app

# copy the requirements and install file
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt


# copy the rest of the application code
COPY . .

# expose the port the app runs on
EXPOSE 8000

# command to run the application
CMD ["uvicorn", "insurance:app", "--host", "0.0.0.0", "--port", "8000"]