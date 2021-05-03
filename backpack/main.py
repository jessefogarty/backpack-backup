from backpack.backpack import backup
import argparse
import sys

def main():
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

    return 1

sys.exit(main())