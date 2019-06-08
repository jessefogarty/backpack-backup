#!/usr/bin/env python3

import os
from distutils.dir_util import copy_tree
from termcolor import cprint
from utils.encrypt import dir_encrypt
from utils.backup import dir_backup
import argparse
from time import sleep

def cli():
    parser = argparse.ArgumentParser(description='Backpack, an easy way to backup a directory.')
    parser.add_argument('path', help='Path to directory', metavar='<PATH>')
    parser.add_argument('--encrypt', help='Encrypt the backup files', action='store_true')
    args = parser.parse_args()
    encrypt = args.encrypt
    path = args.path
    # After dir_backup cwd is changed to /backup/ created
    dir_backup(path)
    sleep(2)
    if encrypt == True:
        dir_encrypt()

if __name__ == "__main__":
    cli()
