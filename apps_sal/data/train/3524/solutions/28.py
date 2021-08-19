def dna_to_rna(dna):
    return ''.join(['U' if x == 'T' else x for x in dna])
