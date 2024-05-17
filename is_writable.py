#!/usr/bin/python3

import sys
import os


def check_if_is_writable(file):
    if text_file.writable():
        print('we can write something into this')
        return True
    else:
        print('this file is not writable')
        return False

text_file = None

if len(sys.argv) > 0:
    text_file = open(sys.argv[1])

if text_file != None:
    check_if_is_writable(text_file)