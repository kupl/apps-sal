def dna_to_rna(dna):
    rna = dna.replace('T', 'U')
    return rna


print(dna_to_rna('GCAT'))
