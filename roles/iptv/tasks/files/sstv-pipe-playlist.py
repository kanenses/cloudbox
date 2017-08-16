#!/usr/bin/env python2.7
from urllib import urlopen

############################################################
# CONFIG
############################################################
PIPE_PATH = "/config/sstv-pipe-play.py"
EPG_PATH = "/config/data/sstv.xml"


############################################################
# SSTV
############################################################

def build_playlist():
    url = "http://sstv.fog.pt/utc/SmoothStreams.m3u8"
    resp = urlopen(url).read().decode("utf-8")
    return resp.replace("#PATH#", PIPE_PATH)


def fetch_epg():
    url = "http://sstv.fog.pt/feed5.xml"
    resp = urlopen(url).read().decode("utf-8")
    with open(EPG_PATH, "w") as fp:
        fp.write(resp)
    return True


############################################################
# MAIN
############################################################

if __name__ == "__main__":
    # Retrieve and store XML EPG
    fetch_epg()
    # Retrieve and print playlist for tvh
    print(build_playlist())
