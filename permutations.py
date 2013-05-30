#!/usr/bin/python

import os
import itertools


def main():
    no='6'
    calPerm(int(no))
    allPerm(int(no))

def calPerm(no):
    while no >=1:
        perm = no*(no-1)
        no = no - 1
    print perm

def allPerm(no):
    for element in list(itertools.permutations([1,2,3,4,5,6])):
        print ' '.join(map(str,element))
if __name__=="__main__":
    main()
