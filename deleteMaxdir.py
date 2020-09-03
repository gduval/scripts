#!/usr/bin/python

import os
import shutil
 
path = "/mnt/pgc1-backups.d/ai-rds-master/"
max_Files = 7
 
def sorted_ls(path):
    mtime = lambda f: os.stat(os.path.join(path, f)).st_mtime
    return list(sorted(os.listdir(path), key=mtime))
 
del_list = sorted_ls(path)[0:(len(sorted_ls(path))-max_Files)]
 
for dfile in del_list:
    shutil.rmtree(path + dfile)
