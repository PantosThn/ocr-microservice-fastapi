FROM python:3.8-slim

COPY ./entrypoint.sh /entrypoint.sh
COPY ./app /app
COPY ./requirements.txt /requirements.txt

#install whatever is neccery
RUN apt-get update && \
    apt-get install -y \
        build-essential \
        python3-dev \
        python3-setuptools \
        tesseract-ocr \
        make \
        gcc \
    #install the packages
    && python3 -m pip install -r requirements.txt \
    #prunning to make docker as small as possible
    && apt-get remove -y --purge make gcc build-essential \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

#make my entypoint executable
RUN chmod +x entrypoint.sh

CMD [ "./entrypoint.sh" ]