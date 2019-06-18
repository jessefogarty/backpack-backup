Backpack.py - Encrypted Backups Made Easy.
======
**backpack.py** is a script used to make quick encrypted backups of a folder or directory.

Example usage as follows below:

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
## Version
* Version 1.5 (in development)
* Version 1.0

## Contact
* e-mail: jessefogarty@tuta.io
* Twitter: [@twitterhandle](https://twitter.com/jessefogarty "twitterhandle on twitter")

[![Flattr this git repo](http://api.flattr.com/button/flattr-badge-large.png)](https://flattr.com/submit/auto?user_id=username&url=https://github.com/username/sw-name&title=sw-name&language=&tags=github&category=software)
