#!/usr/bin/python
import sys
from Bio import SeqIO

def titv(seq1,seq2):
    '''Calculates the transition/transversion ratio for sequeces of equal length '''
    if len(seq1)!=len(seq2):
        sys.exit(1)
    ##define purines, pyrimidines
    purines     = ['A', 'G']
    pyrimidines = ['C', 'T']

    transitionCount   = 0
    transversionCount = 0 

    for seq1, seq2 in zip(seq1,seq2):
        if seq1!=seq2:
            if seq1 in purines: 
                if seq2 in pyrimidines:
                    transversionCount+=1
                else:
                    transitionCount+=1
            if seq1 in pyrimidines: 
                if seq2 in purines:
                    transversionCount+=1
                else:
                    transitionCount+=1

    
    #print transitionCount
    #print transversionCount

    titvRatio = float(transitionCount)/float(transversionCount)

    print titvRatio
    return titvRatio

if __name__=="__main__":

    fileh = open(sys.argv[1],'r')
    records  = list(SeqIO.parse(fileh, "fasta"))                               
    fileh.close()  

    titvRatio = titv(records[0].seq,records[1].seq) 



