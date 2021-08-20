s = ''


def dna_to_rna(dna):
    ddna = list(dna)
    xy = len(dna)
    for i in range(xy):
        if ddna[i] == 'T':
            ddna[i] = 'U'
        else:
            None
    return s.join(ddna)
