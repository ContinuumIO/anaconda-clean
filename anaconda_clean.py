import os
import shutil
from os.path import isfile, isdir, join
import sys, getopt
from optparse import OptionParser
import argparse
from builtins import input

FILES = ['.anaconda', '.astropy', '.atom', '.continuum', '.bash_profile', '.bash_profile-anaconda.bak', '.bash_profile-anaconda2.bak', '.cache', '.conda', '.condamanager', '.condarc',
'.config', '.cython', '.enthought', '.idlerc', '.glue', '.ipynb_checkpoints', '.ipython', '.jupyter', '.matplotlib', '.python-eggs', '.python_history', '.spyder2', '.spyder2-py3', '.theano']

EXIST = []
valid = False

def get_files(): 
    for x in sorted(os.listdir(os.path.expanduser('~'))):
        if x in FILES:
             EXIST.append(x)

def main():
    get_files()
    for fi in EXIST:
        valid = False
        while(valid == False): 
            delete = input("Delete %s? (Y or N): " %fi ) 
            if(delete == "" or delete == 'y' or delete == 'Y' ):
                path = os.path.expanduser('~/%s' %fi)
                if(isfile(path)): 
                     os.remove(path)
                elif(isdir(path)):
                     shutil.rmtree(path) 
                else:
                     print("Error: Unable to remove %s" %fi)
                print("Removed %s successfully" %fi )
                valid = True 
            elif(delete == "n" or delete == "N"):
                valid = True   
            else: 
                print("Invalid input")


if __name__ == '__main__':
    main()
