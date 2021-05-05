FROM python:3
WORKDIR /combination
COPY . /combination
RUN pip3 install --upgrade pip -r requirements.txt
EXPOSE 5005