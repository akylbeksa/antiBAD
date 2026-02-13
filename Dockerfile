FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# системные зависимости (обычно хватает)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements_gradio.txt /app/requirements_gradio.txt
RUN pip install --upgrade pip && pip install -r /app/requirements_gradio.txt

COPY . /app

# Gradio слушает PORT, который даст платформа
EXPOSE 7860
CMD ["python", "app.py"]
