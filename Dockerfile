FROM python:3
WORKDIR /combination
COPY . /combination
RUN pip3 install --upgrade pip -r requirements.txt
EXPOSE 5005
CMD ["gunicorn", "-b", "0.0.0.0:5005", "app:app"]