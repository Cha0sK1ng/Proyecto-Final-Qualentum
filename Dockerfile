FROM python:3.11

WORKDIR /workspace

RUN apt-get update && apt-get install -y git

COPY requirements.txt dev-requirements.txt ./
RUN pip install --no-cache-dir -r dev-requirements.txt

COPY app/ ./app/
COPY tests/ ./tests/
COPY run.py ./

CMD ["sleep", "infinity"]