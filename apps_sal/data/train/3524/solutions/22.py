def dna_to_rna(dna):
    rna = ''
    for base in dna:
        if base == 'T':
            rna += 'U'
        else:
            rna += base
    return rna
