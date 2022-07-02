#!/usr/bin/env python
# import urllib3
import random
import time
from optparse import OptionParser
from urllib.parse import quote_plus
import socket
import ssl
import requests
import urllib3

options = OptionParser(usage='%prog server [options]',
                       description='Simulate normal user traffic to openssl server')
options.add_option('-p', '--port', type='int', default=443, help='TCP port to direct traffic to (default: 443)')
options.add_option('-d', '--delay', type='int', default=0, help='delay between requests in seconds')
options.add_option('-l', action='store_true', dest='login_only', help='only send login packets')
options.add_option('-v', action='store_true', dest='verbose', help='print results of individual requests')

users = [
    "Hans",
    "Karl",
    "Helmut",
    "Olaf",
    "Barbara",
    "Katharina",
    "Anna",
]

passwds = [
    "KZysSy2lPQE2VrwLDchB",
    "9OVqsbucEuJ8WfWdHezG",
    "fDjrdKKYV6PPfSUWQPgh",
    "uiUIdrm9yyTwEdGHWHfm",
    "A6y4uRFkKQ8duL3N0Pjq",
    "YJMQlJ5OeFDtJ7htRvA8",
    "NHaUPjJR8rJrP3dFw5tD",
]


def do_custom_request(hostname: str, port: int, user: str, passwd: str) -> None:
    context = ssl.SSLContext()
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname, do_handshake_on_connect=False) as ssock:
            buf = b'POST ' + '/login.php'.encode('ascii') + b' HTTP/1.0\n'
            buf += b'Content-Type: application/x-www-form-urlencoded\n'
            buf += b'\n'
            buf += b'username=' + quote_plus(user).encode('ascii') + b'&password=' + quote_plus(passwd).encode('ascii')
            print(buf)
            ssock.send(buf)


def create_requests(host: str, login_only: bool):
    request = [""]
    for i in range(len(users)):
        request.append("https://" + host +
                       "/login.php?user=" + users[i] +
                       "&passwd=" + passwds[i])
    if not login_only:
        for i in range(1, 20):
            request.append("https://" + host + "/index.php")
            request.append("https://" + host + "/impressum.php")
            request.append("https://" + host + "/index.html")

    return request


def main():
    assert len(users) == len(passwds)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    opts, args = options.parse_args()
    if len(args) < 1:
        options.print_help()
        return
    while 1:
            rand = random.randrange(0, len(users))
            requests.post(f'https://{"localhost"}/login.php',
                          data={'user': users[rand], 'passwd': passwds[rand]},
                          headers={'Content-Type': 'application/x-www-form-urlencoded'},
                          verify=False
                          )
            print('request done!')
        # do_custom_request('localhost', opts.port, users[rand], passwds[rand])
        # try:
        #     requests.post(f'https://{host}/login.php',
        #                   data={'user': users[rand], 'passwd': passwds[rand]},
        #                   headers={'Content-Type': 'application/x-www-form-urlencoded'},
        #                   verify=False,
        #                   timeout=.001
        #                   )
        # except requests.exceptions.ReadTimeout:
        #     print('read timeout, that is expected ...')
        # except requests.exceptions.ConnectionError as ce:
        #     print(ce)
        #     raise ce
        # if opts.verbose:
        #     print(req[rand])
            time.sleep(opts.delay)


if __name__ == '__main__':
    main()
