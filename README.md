# anaconda-clean

#### Description
This module removes configuration files that are left behind when uninstalling Anaconda.

#### Usage

First, install the conda package. 

     conda install -c RahulJain anaconda-clean

Then run: 

     clean

This will run through the configuration files/directories on your system and give you the option to delete each one. 

Optional: 
To automatically delete all files and directories, run:

     clean --yes 
     
TO create a backup copy of the file/directory in a .anaconda_backup folder in your home directory, run: 

     clean --backup
