def dna_to_rna(dna):
    dna = list(dna)
    for i in range(len(dna)):
        if dna[i] == 'T':
            dna[i] = 'U'
    return "".join(dna)
