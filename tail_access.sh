#!/usr/bin/env bash

tail -f -n 9999999999  /usr/local/nginx/logs/access.log|sed -u -e 's/^/access.log: /' -
