def dna_to_rna(dna):
    rna = dna.maketrans('T', 'U')
    return dna.translate(rna)
