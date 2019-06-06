#!/usr/bin/env python3

import os
from distutils.dir_util import copy_tree
from termcolor import cprint

orig_dir = input(' Enter the directory you want backed up: ')

if os.path.exists(orig_dir) and os.path.isdir(orig_dir):
        os.chdir(orig_dir)
        abspath = os.getcwd()
        files = os.listdir('.')
        cprint(f' Directory: {abspath} \n Files: {files}', 'yellow')

# New backup directory to be created
new_dir = abspath + '/' + 'backup'

try:
    copy_tree('.', new_dir)
except:
    cprint('Copy of original files failed.', red); pass

os.chdir(new_dir)
new_abspath = os.getcwd() ; new_files = os.listdir('.')
cprint(f' Backup directory: {new_abspath} \n Backup Files: {new_files}', 'green')
