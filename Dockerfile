FROM python:3.11

WORKDIR /workspace

RUN apt-get update && apt-get install -y git

COPY requirements.txt dev-requirements.txt ./
RUN pip install --no-cache-dir -r dev-requirements.txt

CMD ["sleep", "infinity"]