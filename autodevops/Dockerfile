FROM python:3.13-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 APP_VERSION=1.0.0
WORKDIR /app
RUN useradd --system --uid 10001 appuser
COPY app/ /app/
USER 10001
EXPOSE 8080
CMD ["python", "/app/app.py"]
