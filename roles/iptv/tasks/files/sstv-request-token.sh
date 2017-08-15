#!/bin/sh
SITE=viewms
USER=USERNAME
PASS=PASSWORD
curl --silent -X "GET" "https://auth.smoothstreams.tv/hash_api.php?username=$USER&password=$PASS&site=$SITE" | jq -r .hash
