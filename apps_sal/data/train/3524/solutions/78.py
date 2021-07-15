def dna_to_rna(dna):
    x = []
    for i in range(len(dna)):
        if dna[i] == 'T':
            x.append('U')
        else:
            x.append(dna[i])
    return ''.join(map(str, x))
