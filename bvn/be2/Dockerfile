FROM python:3.14 

WORKDIR /app
RUN apt-get update && apt-get install -y python3-pip

RUN pip install poetry
RUN poetry config virtualenvs.create false
COPY pyproject.toml /app/pyproject.toml
RUN poetry install --no-root
COPY app/main.py /app/main.py
RUN chmod +x /app/main.py
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]