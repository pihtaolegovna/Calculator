FROM python:3.9-slim

WORKDIR /app

COPY calculator_gui.py .

RUN apt-get update && apt-get install -y python3-tk && \
    rm -rf /var/lib/apt/lists/*

CMD ["python", "calculator_gui.py"]
