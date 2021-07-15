def dna_to_rna(dna):
    for T in dna:
        dna = dna.replace("T","U")
    return dna
