#!/usr/bin/env python
#
#     setup.py
#     Copyright (c) 2019 Eliott PARIS
#
#Tab=3########################################################################


##### IMPORT #################################################################

from __future__ import print_function

import sys

##############################################################################

class A (object):
   def __init__ (self):
      pass

if sys.version_info < (2, 7):
   print >> sys.stderr, 'This script requires python 2.7 or greater.'
   sys.exit (1)

def main ():
   a = A ()
   print ('python version:', sys.version)
   print ('This script requires python 2.7 or greater.', file=sys.stderr)
   print ('print')
   print ('print')
   line = 'printline'
   print(line, end='')

##############################################################################

if __name__ == '__main__':
   sys.exit (main ())
