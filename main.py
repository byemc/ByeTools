#!/usr/bin/env python3

# import libs
import byetools
import argparse
from random import randint

# adds arguments
parser = argparse.ArgumentParser(description='A suite of tools')
parser.add_argument('--tool', '-t', help='The tool you would like to use.', default='os')
args = parser.parse_args()

if args.tool == 'undertale':
    file0 = str(input("Please enter the location of \"file0\""))
    undertaleini = str(input("Please enter the location of \"undertale.ini\""))
    byetools.undertale.loadsandboxsteam(undertaleini, file0)
elif args.tool == 'os':
    print(byetools.get_os())
else:
    print('Please specifiy a valid tool.')
    import os
    os.system("python main.py -h")
    os.system("python3 main.py -h")
