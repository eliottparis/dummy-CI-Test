#!/usr/bin/env python3
#
#     check.py
#
#Tab=3########################################################################


##### IMPORT #################################################################

import argparse
import logging
import os
import platform
import subprocess
import sys
import json



##############################################################################

if sys.version_info < (2, 7):
   print >>sys.stderr, 'This script requires python 2.7 or greater.'
   sys.exit (1)

PATH_THIS = os.path.abspath (os.path.dirname (__file__))



"""
==============================================================================
Name : parse_args
==============================================================================
"""

def parse_args ():
   arg_parser = argparse.ArgumentParser ()

   arg_parser.add_argument (
      '-q', '--quiet',
      dest = 'logging_level', default = logging.INFO,
      action = 'store_const', const = logging.ERROR,
      help = 'Provides less output.'
   )

   arg_parser.add_argument (
      '-v', '--verbose',
      dest = 'logging_level', default = logging.INFO,
      action = 'store_const', const = logging.DEBUG,
      help = 'Provides more output.'
   )

   return arg_parser.parse_args (sys.argv[1:])



"""
==============================================================================
Name : log_job_name
==============================================================================
"""

def log_job_name (args):

   if 'JOB_NAME' in os.environ:
      logging.info (f"JOB_NAME: {os.environ ['JOB_NAME']}")
   else:
      logging.info ("JOB_NAME not defined")



"""
==============================================================================
Name : check
==============================================================================
"""

def check (args):
   logging.info ("CI checks")

   log_job_name (args)




##############################################################################

if __name__ == '__main__':
   logging.basicConfig (format='%(message)s', level=logging.INFO, stream=sys.stdout)

   try:
      sys.exit (check (parse_args ()))

   except subprocess.CalledProcessError as error:
      print >>sys.stderr, 'Check command exited with %d' % error.returncode
      sys.exit(1)
