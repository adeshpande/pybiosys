#!/usr/bin/python

'''translate RNA file to protein string'''

import os
import sys 

from Bio import Seq 

def translationDict(data):
    ## define protein dictionary 
    map = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"L", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}

    proteinSeq =''
    for line in data:
        for index in xrange(0,len(line)-3,3):
            frame = line[index:index+3]
            #print "frame", frame
            if frame in map:
                if map[frame]!="STOP":
                    proteinSeq += map[frame] 

    print proteinSeq
 

def translationBio(data):
    '''Uses Biopython translate '''
    proteinSeq = ''
    for line in data:
        proteinSeq += Seq.translate(line, table='Standard', stop_symbol='', to_stop=False)
        #proteinSeq += Seq.translate(line)
    print proteinSeq

if __name__=="__main__":
    filename = sys.argv[1]
    fileh = open(filename, 'r')
    data  = fileh.readlines()

    #translationDict(data)
    translationBio(data)


