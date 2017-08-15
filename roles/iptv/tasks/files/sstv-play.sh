#!/bin/bash
TOKEN=$(sh /config/sstv-request-token.sh)
SERVER=deu
SITE=viewms
QUALITY=1
CHANNEL=$1
URL=http://"$SERVER".smoothstreams.tv:9100/"$SITE"/ch"$CHANNEL"q"$QUALITY".stream/playlist.m3u8?wmsAuthSign="$TOKEN"=

ffmpeg -i $URL -codec copy -loglevel error -f mpegts pipe:1
