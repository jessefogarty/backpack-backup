Backpack.py - Encrypted Backups Made Easy.
======
![](https://img.shields.io/badge/python-3.5%20|%203.6%20|%203.7%20|%203.8%20|%203.9-green)

> **backpack** is a python script used to make quick encrypted backups of a folder or directory.

Currently backpack uses GnuPG to encrypt data for a specified recipient. 

### Example Usage

```python
$ python3 backpack.py -p ~/Documents/test -d /Volumes/EXT -e jessefogarty@tuta.io
# Output
$ before-backup.zip: encryption ok
$ SUCCESS! Backup File: /Volumes/EXT/before-backup.zip.gpg
```

```python
$ python3 -p ~/Documents/test1.txt -d /Volumes/EXT -e jessefogarty@tuta.io
# Output
$ Encrypting and moving File: tmp.txt
$ tmp.txt: encryption ok
$ SUCCESS! Backup file: /Volumes/EXT/before/tmp.txt.gpg
```

## Todo
* Updated tests
    * back up to external device
* Rich tui setup 
* Project tidy for package
* Docker build & test

## Version
* v0.0.2 *in development*
* **v0.0.1 (current)**

## Contact
* e-mail: unkwn1@tuta.io
* Twitter: [@jessefogarty_](https://twitter.com/jessefogarty_ "twitterhandle on twitter")

[![Flattr this git repo](http://api.flattr.com/button/flattr-badge-large.png)](https://flattr.com/submit/auto?user_id=jessefogarty&url=https://github.com/jessefogarty/sw-name&title=sw-name&language=&tags=github&category=software)
