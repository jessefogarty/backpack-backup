Backpack.py - Encrypted Backups Made Easy.
======
![](https://img.shields.io/pypi/pyversions/3.svg?style=flat-square)

> **backpack.py** is a python3 module used to encrypt and backup a directory or file for a specified GPG address. It can be run on it's own as a shell script or imported as a python module.

Example usage as follows below:

**Used as a console script**

```python
$ backpack -p ~/Documents/test -d /Volumes/EXT -e jessefogarty@tuta.io
# Output
$ before-backup.zip: encryption ok
$ SUCCESS! Backup File: /Volumes/EXT/before-backup.zip.gpg
```

**Imported backup python function**
```python
from backpack.backpack import backup

backup(p, d, e)
```

## Installation Methods

*Note*: It's important you have they GPG key you want to encrypt your data for already installed to `~/.gnupg`. Later versions will offer to generate if not found. 
* Or, potentially forgo GPG for a dynamic keypair ¯\\_(ツ)_/¯

**Pip**
```sh
pip install Backpack-Backup
```

**Source**
```sh
git clone https://github.com/jessefogarty/backpack-backup.git
cd backpack-backup
python3 setup.py install
```

**Source 2**
```sh
git clone https://github.com/jessefogarty/backpack-backup.git
cd backpack-backup
python3 -m pip install -r requirements.txt
python3 -m backpack
```


## Requirements
* Python 3
* GnuPG
    * GPG key created [(How To)](https://docs.github.com/en/github/authenticating-to-github/generating-a-new-gpg-key)

## Version

* 0.0.2 **Current** *(Alpha)*
    * 0.0.2-1 *(development)*

## Contact
* e-mail: jessefogarty@tuta.io
* Twitter: [@twitterhandle](https://twitter.com/jessefogarty "twitterhandle on twitter")
