FROM python:3.11-slim-buster

RUN apt-get update && apt-get install -y libgl1-mesa-glx libegl1-mesa git libglib2.0-0

WORKDIR /app

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY . ./

EXPOSE 8000

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]