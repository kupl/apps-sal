def dna_to_rna(dna):
    if 'T' not in dna:
        return dna
    else:
        rna = dna.replace('T', 'U')
        return rna
    return
