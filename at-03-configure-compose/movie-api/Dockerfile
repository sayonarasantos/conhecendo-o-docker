FROM python:3.11.3-buster

WORKDIR /project

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 3000

CMD ["uvicorn", "app.main:app", "--host=0.0.0.0","--port=3000"]