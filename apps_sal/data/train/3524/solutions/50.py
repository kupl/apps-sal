def dna_to_rna(dna):
    rna = ''
    for l in dna:
        if l.upper() == 'T':
            rna += 'U'
        else:
            rna += l.upper()
    return rna
