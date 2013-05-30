#!/usr/bin/python

import os
import sys

from Bio import SeqIO
from Bio import SeqUtils

def main(infile):
    
    handle = open(infile,'rU')
    for record in SeqIO.parse(handle, "fasta"):
        
        GCpercent = getGC(record.seq)
        #print record.id + " " + str(GCpercent) + "%"
        print record.id
        print str(GCpercent) + "%"
        ## Biopython 
        #print SeqUtils.GC(record.seq)
    

def getGC(seq):
    '''Calculates GC values '''
    DNAList = list(seq)
    A  = DNAList.count('A')
    T  = DNAList.count('T')
    G  = DNAList.count('G')
    C  = DNAList.count('C')
    tot = A + T + G + C
    GC  = G + C 
    GCpercent = (float(GC)/float(tot))*100

    return GCpercent

if __name__=="__main__":
    main(sys.argv[1])

