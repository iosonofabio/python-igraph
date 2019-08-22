# Install foreign graph packages to test import/export functions on CI
import sys
import subprocess as sp

try:
    runfun = sp.run
except AttributeError:
    runfun = sp.call


# Networkx is installed in tox later on


# Graph-tool
if sys.platform == 'linux':
    runfun('sudo echo "deb http://downloads.skewed.de/apt/bionic bionic universe" >> /etc/apt/sources.list"')
    runfun('sudo echo "deb-src http://downloads.skewed.de/apt/bionic bionic universe" >> /etc/apt/sources.list"')
    runfun('sudo apt-key adv --keyserver keys.openpgp.org --recv-key 612DEFB798507F25')
    if sys.version[0] == '2':
        runfun('sudo apt-get install python-graph-tool')
    else:
        runfun('sudo apt-get install python3-graph-tool')

else:
    print('Graph-tool installation on OSX and Windows missing for now')
