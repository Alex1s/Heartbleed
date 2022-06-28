#!/usr/bin/env bash
ACCESS_LOG_PATH=
ERROR_LOG_PATH=

mkdir -p /run/php
php-fpm7.4
chmod 777 /run/php/* # yeah looks insecure ...

/usr/local/nginx/sbin/nginx  # this will start nginx in the background
echo nginx error ? $?

./tail_access.sh &
./tail_error.sh &

echo started tailing

while true; do sleep 60; done;  # do nothing
