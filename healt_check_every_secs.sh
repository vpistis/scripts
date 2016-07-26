#!/bin/bash
#
# Run a webserver healt_check every EVERY_SECS and
# run MAX_CHECKS cycles.
# Used in a cron command to check web servers.
#
# author: vale.pistis@gmail.com
#

set -x

EVERY_SECS=15
MAX_CHECKS=2400

LOG=~/healt_check.log

count=0

while [ $count -lt $MAX_CHECKS ]
do
    wget http://domain.com/index.html >> $LOG 2>&1
    sleep $EVERY_SECS
    rm index.html
    ((count++))
done
exit 0
