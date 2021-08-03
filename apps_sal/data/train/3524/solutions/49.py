def dna_to_rna(dna):
    translate = {'T': 'U', 'A': 'A', 'C': 'C', 'G': 'G'}
    return ''.join(list(map(lambda x: translate[x], dna)))
