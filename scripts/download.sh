#!/usr/bin/env bash
# download copenhagen networks study data from figshare into data/copenhagen/
# skips files that already exist
# source: https://doi.org/10.6084/m9.figshare.7267433
set -e

mkdir -p "$(dirname "$0")/../data/copenhagen"
cd "$(dirname "$0")/../data/copenhagen"

# usage: download <file name> <figshare file id>
# figshare links use the file id, not the name
download() {
  if [ ! -f "$1" ]; then
    echo "downloading $1"
    # -f fail on http error, -sS no progress bar but show errors, -L follow redirect
    curl -fsSL -o "$1" "https://ndownloader.figshare.com/files/$2"
  fi
}

download bt_symmetric.csv    14000795
download bt_symmetric.README 14039048
download calls.csv           14579972
download calls.README        14127311
download fb_friends.csv      13389320
download fb_friends.README   13389839
download genders.csv         13389440
download sms.csv             14579975
download sms.README          14127308

echo "data ready in data/copenhagen/"
