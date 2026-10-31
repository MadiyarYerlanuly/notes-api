FROM python:3.14-slim

WORKDIR /app
COPY app.py ./

ENV PORT=8080
EXPOSE 8080
USER 1000:1000

CMD ["python3", "app.py"]
