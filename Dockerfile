FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "-m", "streamlit", "run", "src/interface/app.py", "--server.address", "0.0.0.0", "--server.port", "8501"]
