import os
import sys
import shutil
from optparse import OptionParser
from os.path import expanduser, isfile, isdir


FILES = [
    '.anaconda', '.astropy', '.continuum',
    '.conda', '.condamanager', '.condarc',
    '.enthought', '.idlerc', '.glue', '.ipynb_checkpoints', '.ipython',
    '.jupyter', '.matplotlib', '.python-eggs',
    '.spyder2', '.spyder2-py3', '.theano',
]
BACKUP_DIR = expanduser('~/.anaconda_backup')


def get_input(msg):
    if sys.version_info[0] == 2:
        return raw_input(msg)
    else:
        return input(msg)


def delete_file(path):
    if not isdir(BACKUP_DIR):
        os.mkdir(BACKUP_DIR)

    if isfile(path):
        shutil.move(path, BACKUP_DIR)
    elif isdir(path):
        shutil.move(path, BACKUP_DIR)
    else:
        print("Error: Unable to move %s" % path)


def main():
    p = OptionParser(
        usage="usage: %prog [options]",
        description="Deletes anaconda config files & directories")

    p.add_option("-y", "--yes",
                  action="store_true",
                  default=False,
                  help="delete all config files & directories")

    opts, args = p.parse_args()

    if len(args) > 0:
        p.error("No arguments expected")

    for fn in sorted(os.listdir(expanduser('~'))):
        if fn not in FILES:
            continue

        path = expanduser('~/%s' % fn)
        if opts.yes:
            delete_file(path)
            continue

        valid = False
        while not valid:
            res = get_input("Delete %s? (y/n): " % fn).strip().lower()
            if res == 'y':
                delete_file(path)
                valid = True
            elif res == 'n':
                valid = True
            else:
                print("Invalid input: %s" % res)


if __name__ == '__main__':
    main()
