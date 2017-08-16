#!/usr/bin/env python2.7
import os
import sys
from datetime import datetime, timedelta
from json import loads, load, dump
from urllib import urlencode, urlopen

token = {
    'hash': '',
    'expires': ''
}

############################################################
# CONFIG
############################################################
USER = ""
PASS = ""
SITE = "viewms"
SRVR = "deu"
QLTY = 1

############################################################
# MISC
############################################################

TOKEN_PATH = os.path.join(os.path.dirname(sys.argv[0]), 'token.json')


def load_token():
    global token
    if os.path.exists(TOKEN_PATH):
        with open(TOKEN_PATH, 'r') as fp:
            token = load(fp)
    else:
        dump_token()


def dump_token():
    global token
    with open(TOKEN_PATH, 'w') as fp:
        dump(token, fp)


############################################################
# SSTV
############################################################

def get_auth_token(user, passwd, site):
    url = "http://auth.smoothstreams.tv/hash_api.php?" + urlencode({
        "username": user,
        "password": passwd,
        "site": site
    })
    resp = urlopen(url).read().decode("utf-8")
    data = loads(resp)
    if 'hash' not in data:
        sys.exit("There was no hash auth token returned from auth.smoothstreams.tv...")
    else:
        token['hash'] = data['hash'].rstrip('=') + "=="
        token['expires'] = (datetime.now() + timedelta(hours=4)).strftime("%Y-%m-%d %H:%M:%S.%f")
        return


############################################################
# MAIN
############################################################

if __name__ == "__main__":
    # format supplied channel
    if len(sys.argv) < 2:
        sys.exit("No channel argument was supplied....")
    channel = ("0%d" % int(sys.argv[1])) if int(sys.argv[1]) < 10 else sys.argv[1]

    # load and check/renew token
    load_token()
    if not token['hash'] or not token['expires']:
        # fetch fresh token
        get_auth_token(USER, PASS, SITE)
        dump_token()
    else:
        # check / renew token
        if datetime.now() >= datetime.strptime(token['expires'], "%Y-%m-%d %H:%M:%S.%f"):
            # token is expired, renew
            get_auth_token(USER, PASS, SITE)
            dump_token()

    # generate stream url
    url = "http://%s.smoothstreams.tv:9100/%s/ch%sq%s.stream/playlist.m3u8?wmsAuthSign=%s" % (
        SRVR, SITE, channel, str(QLTY), token['hash'])

    # pipe ffmpeg
    os.system("ffmpeg -i %s -codec copy -loglevel error -f mpegts pipe:1" % url)
