# =========================
# Stage 1: Dependency builder
# =========================
FROM python:3.14-slim AS builder

ENV POETRY_VERSION=2.2.1
ENV POETRY_NO_INTERACTION=1
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /build

# Cài Poetry hoàn toàn bên trong Docker
RUN pip install --no-cache-dir "poetry==${POETRY_VERSION}"

# Chỉ copy file khai báo dependency
COPY pyproject.toml .

# Tự tạo poetry.lock bên trong Docker
RUN poetry lock

# Cài dependency
RUN poetry install --only main --no-root


# =========================
# Stage 2: Production
# =========================
FROM python:3.14-slim AS production

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Lấy Python packages đã cài từ builder
COPY --from=builder /usr/local/lib/python3.14/site-packages \
                    /usr/local/lib/python3.14/site-packages

# Lấy executable như uvicorn
COPY --from=builder /usr/local/bin \
                    /usr/local/bin

# Copy source code
COPY app ./app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]