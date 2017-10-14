#!/bin/env python
import argparse

halah = argparse.ArgumentParser(description='Tool for filtering unique words')
halah.add_argument('-i', type=str, action='store', help='Input file name')
halah.add_argument('-o', type=str, action='store', help='Output file name')
zeeb = halah.parse_args()

if zeeb.i and zeeb.o:
    with open(zeeb.i,'r') as fi, open(zeeb.o,'w') as fo:
        d = sorted(set(fi.read().split()))
        fo.write('Filtered list, tools can be found on github: https://github.com/B3yeZ/')
        fo.write('\n'.join([l for l in d]))
