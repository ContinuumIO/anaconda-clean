import os
import sys
import time
from optparse import OptionParser
from os.path import basename, expanduser, isdir, join


FILES = [
    '.anaconda', '.astropy', '.continuum',
    '.conda', '.condamanager', '.condarc',
    '.enthought', '.idlerc', '.glue', '.ipynb_checkpoints', '.ipython',
    '.jupyter', '.matplotlib', '.python-eggs',
    '.spyder2', '.spyder2-py3', '.theano',
]
HOME = expanduser('~')
BACKUP_DIR = join(HOME, '.anaconda_backup',
                  time.strftime("%Y-%m-%dT%H%M%S", time.localtime()))


def get_input(msg):
    if sys.version_info[0] == 2:
        return raw_input(msg)
    else:
        return input(msg)


def delete_file(path):
    if not isdir(BACKUP_DIR):
        print("Backup directory: %s" % BACKUP_DIR)
        os.makedirs(BACKUP_DIR)

    try:
        os.rename(path, join(BACKUP_DIR, basename(path)))
    except OSError:
        print("Error: Unable to move %s" % path)


def find_menu_shortcuts():
    from menuinst.win32 import folder_path
    user_shortcuts_dir = folder_path('user', 'system', 'start')
    menus_to_remove = set()
    for d in os.listdir(user_shortcuts_dir):
        if 'Anaconda' in d:
            menus_to_remove.add(join(user_shortcuts_dir, d))
        elif 'Miniconda' in d:
            menus_to_remove.add(join(user_shortcuts_dir, d))
    return menus_to_remove


def prompt_delete(path, opts):
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

    for fn in sorted(os.listdir(HOME)):
        if fn not in FILES:
            continue
        prompt_delete(join(HOME, fn), opts)

    if sys.platform == 'win32':
        for menu in find_menu_shortcuts():
            prompt_delete(menu)


if __name__ == '__main__':
    main()
