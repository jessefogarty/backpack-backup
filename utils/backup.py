#!/usr/bin/env python3
import os
import sys
from distutils.dir_util import copy_tree
import re
from termcolor import cprint

def dir_backup(path):
    orig_dir = path

    # Check for relative path (~) and expand
    if re.search('~', orig_dir):
        orig_dir = os.path.expanduser(orig_dir)
    else:
        orig_dir = os.path.abspath(orig_dir)

    print(os.path.join(orig_dir, 'backup'))


    # Check if path exists AND IS a directory
    if os.path.exists(orig_dir) and os.path.isdir(orig_dir):
        # Change working directory to orig_dir
        os.chdir(orig_dir)

        # New backup directory to be created
        # TODO: Add check to see if exists! Dir must NOT exist
        new_dir = path.split('/')[-1] + '-backup'

        # Try to copy the dirtree entirely
        try:
            copy_tree('.', new_dir)
        except:
            cprint('Copy of original files failed.', red); pass

        os.chdir(new_dir)
        new_files = os.listdir('.')
        cprint(f' Successfully backed up: {orig_dir}! Details below. \n Backup directory: {os.path.abspath(new_dir)} \n Backup Files: {new_files}', 'green')


    else:
        print(f'Cannot find directory: {orig_dir}')
