#!/usr/bin/env python

import time,getpass
import requests, json
import string
import re

LOGIN_FILE = 'login.txt'
URLS_FILE = 'poll-urls.txt'

def readlines(filename): return [line.strip() for line in open(filename)]

(USERNAME, PASSWORD) = readlines(LOGIN_FILE)
IN_OUT = map(string.split, readlines(URLS_FILE))

HEADERS = {'user-agent': '/u/dbzer0\'s transparency python bot', }

#----------------------------------------------------------------------
def login(username, password):
    """logs into reddit, saves cookie"""

    #print 'begin log in'
    #username and password
    UP = {'user': username, 'passwd': password, 'api_type': 'json',}

    #POST with user/pwd
    client = requests.session()
    r = client.post('http://www.reddit.com/api/login', data=UP, headers=HEADERS)

    #if you want to see what you've got so far
    #print r.text
    #print r.cookies

    #gets and saves the modhash
    j = json.loads(r.text)
    client.modhash = j['json']['data']['modhash']
    #print '{USER}\'s modhash is: {mh}'.format(USER=USERNAME, mh=client.modhash)

    #pp2(j)

    return client


client = login(USERNAME, PASSWORD)

def valid_result(s):
        match = re.search('<title>Too Many Requests</title>|<title>Ow! -- reddit.com</title>', s, re.I)
        return not match

for in_out in IN_OUT:
        URL = in_out[0]
        WEBPATH = in_out[1]

        url = r'{}'.format(URL)

        time.sleep(10)
        r = client.get(url, headers=HEADERS)

        if valid_result(r.text):
                with (open(WEBPATH,"w")) as out:
                        out.write(r.text.encode('utf8'))
                print "Succesfully mirrored %s" % URL
        else:
                print "Error fetching %s" % URL
