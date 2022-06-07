import random
import time
from optparse import OptionParser
import requests

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
    opts, args = options.parse_args()
    if len(args) < 1:
        options.print_help()
        return
    host = args[0] + ":" + str(opts.port)
    req = create_requests(host, opts.login_only)
    while 1:
        rand = random.randrange(1, len(req))
        r = requests.get(req[rand], verify=False)
        if opts.verbose:
            print(req[rand])
            print(r)
        time.sleep(opts.delay)


if __name__ == '__main__':
    main()
