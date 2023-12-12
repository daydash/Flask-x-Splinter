FROM python

COPY requirements.txt requirements.txt
COPY testing_selenium_locally.py testing_selenium_locally.py
COPY testing_splinter.py testing_splinter.py
COPY app.py app.py

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python", "app.py" ]