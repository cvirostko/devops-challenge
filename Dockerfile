FROM python:3.7.9-slim
WORKDIR /code
COPY . .
RUN pip3 install -r requirements.txt
CMD python integration.py