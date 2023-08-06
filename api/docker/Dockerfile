FROM python:3.10


WORKDIR /app
ENV PYTHONPATH "${PYTHONPATH}:/app/src"

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]