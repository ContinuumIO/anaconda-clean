# anaconda_clean

#### Description
This module removes configuration files that are left behind when uninstalling Anaconda.

#### Usage

First, install the conda package. 

     conda install -c RahulJain anaconda_clean

Then, in your Python interpreter, run: 

     import anaconda_clean as ac
     ac.main()

This will run through the configuration files installed on your system and give you the option to delete each one. 
