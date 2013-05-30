import os
import sys
import re

from Bio import SeqIO

from translationSimple import translationBio 

def spliceBio(records):
    '''Splices the data in BioPython records'''
    querySeq = records[0].seq
    #print querySeq
    for i in xrange(1,len(records)):
        intron   = records[i].seq
        #print 'intron',type(intron)
        ## Splice our intron  
        querySeq = re.sub(str(intron),'',str(querySeq)) 
    #print querySeq
    return querySeq

if __name__=="__main__":
    fileh    = open(sys.argv[1], 'rU')
    records  = list(SeqIO.parse(fileh, "fasta"))
    fileh.close()
    
    querySeq   = spliceBio(records)
    queryList  = []
    queryList.append(querySeq)
    ## translate list of DNA strings
    proteinSeq = translationBio(queryList)
    print proteinSeq

