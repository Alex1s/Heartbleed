#!/usr/bin/env bash

tail -f -n 9999999999  /usr/local/nginx/logs/error.log|sed -u -e 's/^/error.log: /' -
