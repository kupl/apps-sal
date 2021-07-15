def dna_to_rna(dna):
    rna = []
    if 'T' in dna:
        dna = dna.replace('T', 'U')
    return dna
