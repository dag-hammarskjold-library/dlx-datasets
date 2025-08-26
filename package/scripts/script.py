# This is meant to be run from the command line. It can be configured to be
# installed as a CLI command using the 'entry_points' parameter in setup.py 

import sys
from argparse import ArgumentParser
from package.module import Class # rename package, module and class

def get_args():
    parser = ArgumentParser()
    parser.add_argument('--arg', help='')

    return parser.parse_args()

def run():
    args = get_args()
    c = Class()
    c.hello_world()

    return

###

if __name__ == '__main__':
    run()