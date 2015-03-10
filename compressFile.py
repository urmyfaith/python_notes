# -*- coding: utf-8 -*-


import os
import sys
import time

dirNames=os.listdir(os.getcwd())

for dir in dirNames:
    if os.path.isdir(dir):
        cmd = "tar cvf " + dir +".tar" + " "+dir
        os.system(cmd)