FROM python:3.8-slim

COPY ./entrypoint.sh /entrypoint.sh
COPY ./app /app
COPY ./requirements.txt /requirements.txt

#install whatever is neccery
RUN python3 -m venv /opt/venv && /opt/venv/binb/python -m pip install -r requirements.txt
    #prunning to make docker as small as possible
    #&& apt-get remove -y --purge make gcc build-essential \
    #&& apt-get autoremove -y \
    #&& rm -rf /var/lib/apt/lists/*

#make my entypoint executable
#RUN chmod +x entrypoint.sh

#CMD [ "./entrypoint.sh" ]