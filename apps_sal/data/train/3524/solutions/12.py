def dna_to_rna(dna):
    rna = []
    for base in dna:
        if base == 'T':
            rna.append('U')
        else:
            rna.append(base)
    return ''.join(rna)
