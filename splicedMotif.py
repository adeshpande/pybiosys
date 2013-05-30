import sys
import re

from Bio import SeqIO

def splicedMotif(records):
    ''' '''
    seq = records[0].seq    
    sub = records[1].seq

    pattern = ".*".join(sub)
    print seq
    print pattern
    match   = re.search(pattern,str(seq))
    print match
    #print match.start()
    #print match.end()


if __name__=="__main__":
    fileh    = open(sys.argv[1], 'rU')                                         
    records  = list(SeqIO.parse(fileh, "fasta"))                               
    fileh.close()
    splicedMotif(records)
