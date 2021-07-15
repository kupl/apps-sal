def dna_to_rna(dna):
    d = {'T': 'U'}
    return ''.join([d.get(i, i) for i in dna])
