def dna_to_rna(dna):
    for i in range(len(dna)):
        if dna[i] == 'T':
            dna = dna[:i] + 'U' + dna[i + 1:]
    return dna
