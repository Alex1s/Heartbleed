#!/usr/bin/env bash
ACCESS_LOG_PATH=
ERROR_LOG_PATH=

/usr/local/nginx/sbin/nginx  # this will start nginx in the background
echo nginx error ? $?

./tail_access.sh &
./tail_error.sh &

echo started tailing

while true; do sleep 60; done;  # do nothing
