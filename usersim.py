#!/usr/bin/env python
# import urllib3
import random
import time
from optparse import OptionParser
import requests
import urllib3

options = OptionParser(usage='%prog server [options]',
                       description='Simulate normal user traffic to openssl server')
options.add_option('-d', '--delay', type='int', default=0, help='delay between requests in seconds')

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


def main():
    assert len(users) == len(passwds)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    opts, args = options.parse_args()
    if len(args) < 1:
        options.print_help()
        return
    while 1:
            rand = random.randrange(0, len(users))
            requests.post(f'https://{args[0]}/login.php',
                          data={'username': users[rand], 'password': passwds[rand]},
                          headers={'Content-Type': 'application/x-www-form-urlencoded'},
                          verify=False
                          )
            print('request done!')
            time.sleep(opts.delay)


if __name__ == '__main__':
    main()
