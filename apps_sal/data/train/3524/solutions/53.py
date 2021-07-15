def dna_to_rna(dna):
    return ''.join(map(lambda a: 'U' if a is 'T' else a, dna))
