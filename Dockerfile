FROM pytorch/torchserve:latest-cpu

WORKDIR /code/

COPY ./requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt

COPY . /code
CMD ["torchserve", "--start", "--model-store", "model-store", "--models", "TEST1=TEST1.mar", "--ncs"]