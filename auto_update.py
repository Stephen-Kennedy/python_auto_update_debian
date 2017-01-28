#!/usr/bin/env python3
# Author: Stephen Kennedy
# 2017_01_14
import os

d = '/opt/bin/'  # directory path for update file to reside
f = d + 'autoupdate.py' # file to check for updates

# Check to see if /opt/bin directory exists. If not,
# create it.

if not os.path.exists(d):
        os.makedirs(d)

# configure file for future autoupdates to place in /opt/bin
if not os.path.isfile(f):
        fo = open(f, 'w')
        fo.write('#!/usr/bin/env python3 \n')
        fo.write('import os \n')
        fo.write('\n')
        fo.write("os.system('apt-get update -y') \n")
        fo.write("os.system('apt-get upgrade -y') \n")
        fo.write("os.system('apt-get autoremove -y') \n")
        fo.close()
        os.chmod(f, 775)

# run auto-update
os.system(f)
