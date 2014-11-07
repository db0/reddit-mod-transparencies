import time,getpass
import requests, json
from pprint import pprint as pp2

USERNAME = "anarchobot"
WEBPATH = "/web/transparency.dbzer0.com/modlog/anarchism/index.html"
PASSWORD = "[PASSWORD]"
URL = "http://www.reddit.com/r/Anarchism/about/log/"

#----------------------------------------------------------------------
def login(username, password):
    """logs into reddit, saves cookie"""

    #print 'begin log in'
    #username and password
    UP = {'user': username, 'passwd': password, 'api_type': 'json',}
    headers = {'user-agent': '/u/dbzer0\'s transparency python bot', }

    #POST with user/pwd
    client = requests.session()
    r = client.post('http://www.reddit.com/api/login', data=UP)

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

#mod mail url
url = r'{}'.format(URL)
r = client.get(url)

#here's the HTML of the page
#pp2(r.text)

#Writing the result onto the file
pp2(r.text, open(WEBPATH,"w"))
