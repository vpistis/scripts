#!/bin/bash
#
# Change part of destination path of a symlink
# 
# thanx to: http://stackoverflow.com/a/25567429/5941790
#

DIR=/home/ubuntu/
SYMLINKS=`find $DIR -maxdepth 1 -type l -print | tr -s ' '  | cut -d ' ' -f9`
OLD_PATH=pippo
NEW_PATH=pluto

for l in $SYMLINKS;
do
    ln -f -s -T `readlink "$l"  | sed 's/$OLD_PATH/$NEW_PATH/' ` "$l"
    echo "$l"
    echo ls -altrh "$l"
done
