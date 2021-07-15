def dna_to_rna(dna):
    for t in dna:
        if t == 'T':
            dna = dna.replace('T', 'U')
    return dna
