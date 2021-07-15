def dna_to_rna(dna):
    rna = []
    for x in dna:
        if x == 'T':
            rna.append('U')
        else:
            rna.append(x)
    return ''.join(rna)

