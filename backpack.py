#!/usr/bin/env python3

import os
from distutils.dir_util import copy_tree
from termcolor import cprint
import gnupg
import shutil
import argparse
from time import sleep
import re

def cli():
    parser = argparse.ArgumentParser(description='Backpack, an easy way to backup a directory.')
    parser.add_argument('path', help='Path to directory', metavar='<PATH>')
    parser.add_argument('--encrypt', help='Encrypt the backup files \n requires --email', action='store_true')
    parser.add_argument('-email', help='Encrypt for recipient GPG email',)
    args = parser.parse_args()
    encrypt = args.encrypt ; path = args.path ; email = args.email
    # After dir_backup cwd is changed to /backup/ created
    #dir_backup(path)
    #sleep(2)
    if encrypt == True and email == None:
        print('ERROR: --encrypt requires --email <EMAIL> ')
        exit()
        #dir_encrypt()


def check_path(path):
    if re.search('~', path):
        path = os.path.expanduser(path)
    else:
        path = os.path.abspath(path)
    return path

def backup(path, dest, email):

    orig_dir = check_path(path)

    dest = check_path(dest)

    # Check if path exists AND IS a directory
    if os.path.exists(orig_dir) and os.path.isdir(orig_dir):
        # New backup directory to be created
        # TODO: Add check to see if exists! Dir must NOT exist
        dir_name = path.split('/')[-1] + '-backup'

    # Check for existing (dir)-backup - ask to delete
    # TODO: Add check for existing (dir)-backup.zip - ask to delete
    dest_folder = str(dest + "/" + dir_name)
    if os.path.exists(dest_folder) and os.path.isdir(dest_folder):
        print('Detected existing backup. Delete and continue?')
        overwrite = input('Selection [Y/N]: ')
        if not overwrite.upper() in 'Y':
            exit()
        else:
            shutil.rmtree(dest_folder)

    os.mkdir(dest_folder)

    # BEGIN FILE encryption
    os.chdir(path)

    # Location for the user's GPG settings
    gpg = gnupg.GPG(gnupghome=os.path.expanduser('~/.gnupg'))
    # Prepare file(s) in directory for encryption
    files_dir = []
    files = [f for f in os.listdir(".") if os.path.isfile(f)]
    for f in files:
        files_dir.append(f)
    for x in files_dir:
        with open(x, mode='rb') as f:
            # output = [file_name].gpg
            status = gpg.encrypt_file(f, recipients=email, output=x+".gpg")
            status_msg = f'{x}: {status.status}'
            cprint(status_msg, 'green')
            # move output to destination folder
            dfile = x+'.gpg'
            efile = dest_folder+'/'+x+'.gpg'
            os.rename(dfile, efile)


    # Compress backup folder
    os.chdir(dest)
    # zip archive will be stored in dest
    shutil.make_archive(dir_name, 'zip', root_dir=dir_name)
    dest_archive = dest+'/'+dir_name+'.zip'
    # delete uncompressed directory (dest_folder)
    shutil.rmtree(dest_folder)
    print(f'Successfully created {dest_archive}')

if __name__ == "__main__":
    path = '/Volumes/EXT/before'
    dest = '/Volumes/EXT'
    email = 'jessefogarty@tuta.io'
    backup(path, dest, email)
