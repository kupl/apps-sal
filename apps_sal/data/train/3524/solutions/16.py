def dna_to_rna(dna):
    rna = ''
    for base in dna:
        if base != 'T':
            rna += base
        else:
            rna += 'U'
    return rna
