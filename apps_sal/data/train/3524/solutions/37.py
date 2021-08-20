def dna_to_rna(dna):
    rna = ''
    for x in dna:
        if x == 'T':
            rna += 'U'
        else:
            rna += x
    return rna
