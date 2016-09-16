import sys
from distutils.core import setup


if sys.version_info < (2, 7):
    sys.exit("Sorry, this only works on Python 2.7, 3+")


setup(
    name='anaconda-clean',
    version='1.0',
    author='Continuum Analytics',
    license='BSD',
    description='Delete Anaconda config files',
    py_modules=['anaconda_clean'],
)
