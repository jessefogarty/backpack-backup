#!/usr/bin/env python3
""" A program that will encrypt and archive a file or directory.
        - Uses GPG 
"""
import os
from typing import Dict, Tuple
from termcolor import cprint
import gnupg
import shutil
import argparse
import re
import sys


def cli():
    """The CLI for the program."""
    parser = argparse.ArgumentParser(
        description="Backpack, an easy way to backup a directory."
    )
    parser.add_argument(
        "-p", help="Path to file or directory", metavar="<PATH>", required=True
    )
    parser.add_argument(
        "-d", help="Path to destination directory", metavar="<PATH>", required=True
    )
    parser.add_argument(
        "-e", help="GPG Email for encryption", metavar="<john@gmail.com>", required=True
    )
    args = parser.parse_args()
    path: str = args.p
    dest: str = args.d
    email: str = args.e
    backup(path, dest, email)


def full_path(p: str) -> str:
    """Expand a relative path and return the absolute path.

    Args:
        p (str): the relative path to a file.
    Returns:
        p (str): the absolute path to a file
    """
    if re.search("~", p):
        p = os.path.expanduser(p)
    else:
        p = os.path.abspath(p)
    return p


def encrypt(z: str, e: str) -> None:
    """Encrypts an archive file for a specifid recipient using GPG.

    Args:
        z: str - absolute path to zip archive file you want to encrypt.
    Returns:
        e: str - absolute path to encrypted zip archive file (.zip.gpg).
    """

    # See if default location exists (assuming the key is too)
    # if NOT found ask to create
    if os.path.exists(os.path.expanduser("~/.gnupg")) is False:
        cprint("ERROR! No '~/.gnupg' directory found.", "red")
        _new: str = input("Create a new key and default directory? [y/N]: ").upper()
        if _new == "Y":
            name: str = input("Enter your full name: ").capitalize()
            email: str = input("Enter your email address: ").lower()
            key_lengh: int = 4096
            comment: str = input("Enter a comment: ").lower()
            password: str = input("Enter a passphrase: ")
        # if N or any other input exit
        else:
            sys.exit()

    # Begin encryption of data
    gpg = gnupg.GPG(gnupghome=os.path.expanduser("~/.gnupg"))
    with open(z, mode="rb") as f:
        # output = [file_name].gpg
        status = gpg.encrypt_file(f, recipients=e, output=z + ".gpg")
        status_msg = f"{z}: {status.status}"
        cprint(status_msg, "green")


def new_key(**kwargs: str) -> Dict:
    """ Creates a new GPG key.
    
    Args:
        name = str
        email = str
        password = str
    """
    key_default: Dict = {
       "name": "Backpack Backup",
       "email": "backpack@unkwn1.dev",
       "key_type": "RSA",
       "key_length": 4096,
       "comment": "default generated GPG key by Backpack Backup",
       "password": ("no_protection", False)
   }

   # If 3 args provided merge dicts
    if len(kwargs) > 0:
        if "name" and "email" and "password" in kwargs:
            key_default |= kwargs
    
    gpg = gnupg.GPG()

    key_data = gpg.gen_key_input(**key_default)

    # No args or not 3 required -> use default
    return key_default

def backup_dir(p: str, d: str) -> str:
    """Create a zipped copy of a directory.

    Args:
        p: str - full path to file or directory to backup.
        d: str - full path to the destination for the backup archive file.
    Returns:
        z: str - full path to backup archive OR archive object.
    """
    # dest_name = name for backup directory
    dest_name = p.split("/")[-1] + "-backup"
    # create zip
    z = shutil.make_archive(dest_name, "zip")
    # move zip from cwd to dest
    os.rename(z, d + "/" + z)
    # encrypt zip then delete it
    os.chdir(d)
    return z


def backup(path: str, dest: str, email: str) -> None:
    """Backup and encrypt a file or directory to a destination.
    *Backed up data is encrypted for the email user provided*.

    Args:
        path: str - relative path to original data.
        dest: str - relative path to desination directory.
        email: str - email of GPG recipient.
    """

    # Expand ~/ or ensure absolute path
    orig_dir = full_path(path)
    dest = full_path(dest)

    # if orig_dir{path}; zip and backup to dest
    # TODO: wrap if in try. Except = os.path.exists. Move else after except as catchall error
    if os.path.isdir(orig_dir):
        # TODO: check if backup zip already exists before z
        #   overwrite = input('Selection [Y/N]: ')
        #   if not overwrite.upper() in 'Y':
        os.chdir(orig_dir)

        # backup(orig_dir, dest)
        # dest_name = name for backup directory
        z = backup_dir(orig_dir, dest)
        # encrypt zip then delete it
        os.chdir(dest)
        encrypt(z, email)
        print(f'SUCCESS! Backup File: {dest+"/"+z+".gpg"}')
        os.remove(z)

    # File backup if no dir found
    elif os.path.exists(orig_dir):
        dir_path = os.path.dirname(orig_dir)
        fname = orig_dir.split("/")[-1]
        ename = fname + ".gpg"
        print(f"Encrypting and moving File: {fname}")
        os.chdir(dir_path)
        encrypt(fname, email)
        os.rename(ename, dest + "/" + ename)
        print(f'SUCCESS! Backup file: {dest+"/"+ename}')
    else:
        raise IOError(f"{orig_dir} Not Found! ")


# launch cli if called
if __name__ == "__main__":
    cli()
