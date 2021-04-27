#!/usr/bin/env python3


import shutil

import os

#change to my home directory

os.chdir('/home/student/mycode/')

#move the file to names directory

shutil.move('raynor.obj', 'ceph_storage/')

#input to the new name

xname = input('What is the new name for kerrigan.obj? ')

#rename the file or move it too

shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)



