import os
import shutil
from optparse import OptionParser
from os.path import isfile, isdir


FILES = ['.anaconda', '.astropy', '.atom', '.continuum', '.bash_profile', '.bash_profile-anaconda.bak', '.bash_profile-anaconda2.bak', '.cache', '.conda', '.condamanager', '.condarc',
'.config', '.enthought', '.idlerc', '.glue', '.ipynb_checkpoints', '.ipython', '.jupyter', '.matplotlib', '.python-eggs', '.python_history', '.spyder2', '.spyder2-py3', '.theano']

EXIST = []
backup_file = False

def get_files():
    for x in sorted(os.listdir(os.path.expanduser('~'))):
        if x in FILES:
             EXIST.append(x)


def delete_file(path):
    if(isfile(path)):
        if(backup_file):
            shutil.move(path, dirpath)
        else:
            os.remove(path)
    elif(isdir(path)):
        if(backup_file):
            shutil.move(path, dirpath)
        else:
            shutil.rmtree(path)
    else:
        print("Error: Unable to remove %s" %fi)


def main():
    get_files()
    p = OptionParser(
        usage="usage: %prog [options]",
        description="Deletes anaconda config files & directories")
    p.add_option("-y", "--yes",
                  action="store_true",
                  dest="delete_all",
                  default=False,
                  help="delete all config files & directories")
    p.add_option("-b", "--backup",
                 action="store_true",
                 dest="backup",
                 default="False",
                 help="create a backup folder of deleted files")
    opts, args = p.parse_args()

    if(opts.backup):
        global backup_file
        backup_file  = True
        global dirpath
        dirpath = os.path.expanduser('~')
        dirpath= os.path.join(dirpath, '.anaconda_backup')
        if not os.path.exists(dirpath):
            os.makedirs(dirpath)

    if(len(args) > 0):
        p.error("No arguments expected")

    for fi in EXIST:
        path = os.path.expanduser('~/%s' %fi)
        if(opts.delete_all):
            delete_file(path)
        valid = False
        while(valid == False):
            delete = raw_input("Delete %s? (Y or N): " %fi )
            if(delete == "" or delete == 'y' or delete == 'Y' ):
                delete_file(path)
                valid = True
            elif(delete == "n" or delete == "N"):
                valid = True
            else:
                print("Invalid input")


if __name__ == '__main__':
    main()
