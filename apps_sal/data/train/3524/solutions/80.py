#! python3

def dna_to_rna(dna):
    rna = ''
    for i in dna:
        if i == 'T':
            rna = rna + 'U'
        else:
            rna = rna + i
    return rna
