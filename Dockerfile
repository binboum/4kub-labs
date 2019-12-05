FROM python:3.8.0-slim-buster
COPY . /lab
WORKDIR /lab
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["lab.py"]