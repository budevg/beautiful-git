#!/usr/bin/python

import urllib
import re
import argparse
import os
import sys

def next_commit_msg():
    '''Return next coommit message which should be descriptive and
    easy to understand'''
    try:
        data = urllib.urlopen("http://whatthecommit.com").read()
        m = re.search("<p>(.*?)</p>", data, re.S)
        return m.group(1).strip()
    except:
        return "I'm Feeling Lucky"

def main():
    parser = argparse.ArgumentParser(
        description='Make your git commits readable to humans (programmers ?).')
    parser.add_argument("-m",
                        dest="message",
                        action="store_true",
                        default=False,
                        help="generate commit message")
    args = parser.parse_args()
    if args.message:
        print next_commit_msg()
    else:
        cmd = ("git filter-branch -f --msg-filter '%s -m'" %
               os.path.realpath(sys.argv[0]))
        print "Amazing physics going on..."
        os.system(cmd)

if __name__ == '__main__':
    main()
