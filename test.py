#!/usr/bin/env python
#
#     setup.py
#     Copyright (c) 2019 Eliott PARIS
#
#Tab=3########################################################################


##### IMPORT #################################################################

from __future__ import print_function

import os
import subprocess
import sys

if sys.version_info < (2, 7):
   print >> sys.stderr, 'This script requires python 2.7 or greater.'
   sys.exit (1)

##############################################################################

class A (object):
   def __init__ (self):
      pass

def main ():
   a = A ()
   print ('- test.py => python version:', sys.version)

   if 'TRAVIS' in os.environ:
      print ('Running on Travis-CI')
      if 'TRAVIS_PYTHON_VERSION' in os.environ:
         print ('TRAVIS_PYTHON_VERSION:', os.environ ['TRAVIS_PYTHON_VERSION'])
      else:
         print ('TRAVIS_PYTHON_VERSION undefined')

   returncode = 50
   print ('test error', returncode, file=sys.stderr)
   print ('print')

   print ('############')
   line = 'printline'
   print (line, end=' ')
   print ('end')

   print ('############')
   python_exe = sys.executable
   print ('python_exe:', python_exe)

   cmd = [python_exe, 'sub.py']
   subprocess.check_call (cmd)

##############################################################################

if __name__ == '__main__':
   sys.exit (main ())
