FROM python:3.10.0-alpine

COPY . /
ARG IP_ADDRESS
ENV API_KEY=${API_KEY}

COPY ./requirements.txt /
COPY ./app.py /
COPY ./entrypoint.sh /

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD ["192.168.3.1"]
