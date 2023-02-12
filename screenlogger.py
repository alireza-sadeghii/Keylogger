from mss import mss
from datetime import datetime
import os
from time import sleep


#
# takes one screenshots each minute
#
def take():
    screen_viewer = mss()
    dirName = datetime.now().strftime("%Y-%m-%d")
    make_directory(dirName)
    os.chdir(dirName)
    while True:
        file_name = datetime.now().strftime("%H \' %M \' %S") + ".png"
        screen_viewer.shot(mon=-1, output=file_name)
        sleep(60)


#
# makes a directory for screenshots of each day
#
def make_directory(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)
