FROM alpine

LABEL maintainer "Alexey Nizhegolenko <ratibor78@gmail.com>"
LABEL description "Kubyk app template, Alpine Linux managed by Supervisord"


# Copy the requirements file
COPY requirements.txt /tmp/requirements.txt

# Install all needed packages
RUN apk add --no-cache \
    python3 \
    bash \
    nginx \
    uwsgi \
    uwsgi-python \
    supervisor && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    pip3 install -r /tmp/requirements.txt && \
    rm /etc/nginx/conf.d/default.conf && \
    rm -r /root/.cache && \
    mkdir /IO_PROJECT


# Copy the application files
COPY ./app /IO_PROJECT/app
COPY ./io.py config.py /IO_PROJECT/

# Copy Sqlite base with users data
COPY ./sqlite /IO_PROJECT/sqlite

# Copy Nginx default config
COPY nginx.conf /etc/nginx/

# Copy Supervisord config
COPY supervisord.conf /etc/supervisord.conf

# Copy uwsgi config
COPY uwsgi.ini /etc/uwsgi/

# Copy the nginx config for the app
COPY kubyk-nginx.conf /etc/nginx/conf.d/

# Specify the listening port
EXPOSE 80

# Run our app using Supervisord
CMD ["/usr/bin/supervisord"]
