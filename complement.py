#!/usr/bin/python

'''Find the compliment'''

def complement(sequence):
    complement = {"A":"T", "T":"A", "C":"G", "G":"C", "N":"N"}
    reverse_complement_sequence = ""
    sequence_list = list(sequence)
    sequence_list.reverse()

    for letter in sequence_list:
        reverse_complement_sequence += complement[letter.upper()]
    print reverse_complement_sequence


if __name__=="__main__":
#    Str = "CTCAATAATGACTCTGAATCCCGGTCATCCTAGGTGCTAGTCGGCTTAGTGCACGGTAATATCGCTAGATCGAGCTCGGCATGGATATCCTCTACACTTTTGCCGACGACTACCGCCCCATGCAAGCTGAAGAAACATTAATGCTCCATCGCTAGAGTAGACCACAGAGTTTCGGAACCGTACTTTTACGTCAAGTCTAACGCGAGTCGGGATCCGCCCCGTTACACGTTAAGACTCCTAGGGCTTAATACGGCACGACGCCGGCAAAAATCCAGTCCTTCAAAAAGTAGGTCCGTGGCCCTCGTCTACTATATTCGACTTCTCACAACCTGAATCGACTCGAACCTGCAATTTCCGGAATTCTCCTTGCTTAGAGCTACCGAAGCTATGCCACCCACACCGGTCATGTCGTCTCCTCGACATCCCCGTTGTGTTCTACAACGTTTCCTCCGGATTTCCTGCTAATTGTCCTAGACGAGCTGCCGGCGAGTCTTCCAACGGTATGTAGAAAACGCTGTTAAATCTAAGCCTGACTATAATGGTCCGAGGAGAGCAAGTCGCACGATGGGCCACTTGTCCTGTGGCAGAAGAAAAGAGAACCCGATAAGTCGTTTTAAACCTAGCTAAGAGATAAGGTTGACGGACATGGAGTTTTAGGATCACACGTGTAGCTTGCGTCACAGATTTGCCTGTGTGATTTCTAATGGATCTGCCTGGGTCATAGGGTGATTTCAGTTGATACCCACGTAACTCTTGGCGTGCTTGAAGTAGATATGTCCCCAACGGACTGCTAGCGCAATACCCTGAAGCAGGCCTTCCGTTATAGTCTGGTCATCTTAATTATACCAGTGGCCACATAGACGTATAGCTTTATCCGGCACGCA"
    Str= "TTTGGTCTATCAAGTCAGGTCTGTCAGAGCGTCCTGTCTCAGCTTTGTTATCATGCTTGGCACTTTAAACTGTTTGTAGTTAGAGGAGCCGCGACGCTGATAGTATGCTTTGCAGGTCGCAGGCGTCAGGGAGACCAAATAGTACATATGTGGACGACGCTGCGTGCAAAGGGTCGTGAAATGCCGAACGGTCTCTTTTCAGTAGGTGCAGGGGGAAATTCAAGAGCTAACTTGAGAATAGCGGGTGTACAGGTTTACGTGGCGAGCCCGGTTTCGTGCGCGTCGTGATACGGTCTGGTGGGTAGAGCGATGGTCGTGCTATATAAAAATACGAGCCCTCAGGGCTCCGATCACGCTTTGGGTCGCATTGCGGCAGAATGGCTCGAATCTGACACCGTAACTGAACGAGGAGGGGCATACGGCGGTCAACTATACCAAGGCTCACATGCGGTCGTCCGGAAGTATAGGGTGACGATTAGTCAGCTTAAACGGTATGGTCTCCCCTTCCCGGCATTGCTCGACGTGATGCTCATGTGAGACGTAAGGTCCGTTCCCGGAAATAGCATAGTTGGTGAGGAATGAACATTCCTATACCTTTAAATCGTTCTGATGGAAATGTAGGCCTTTTAAGACGGTTGGACATCAAGAAGAAAATGGTCCTCCTTAAGGATGATAATTTTAAATCAGTAAATACAGTTGCCATTCACAGTGTGAGCTATCTTCTACAAAGACTGTCGTCGGAACAGGCGTGGCTAGGTTGTCTAACTCGCAATTTATATTAGCCGGGAAATTAACCCGTCTAAGAGGGTTGCCGTATTCCATCGGCGACAGGTGGTTTTCATTTCAGGCGCGCATGTCCAACAAGCTGTCTTCTGCTCCCATCCCGCATGCGACGGTTCAATCCTCACGGTCACGATTTCTCACTGGACTTGAACCATAAATTTTGGGACTTGGATAACCGAAGTTGAGTCTTACACA"
    complement(Str)
