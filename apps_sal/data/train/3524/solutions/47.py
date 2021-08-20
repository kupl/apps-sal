def dna_to_rna(dna):
    import re
    return re.sub('T', 'U', dna)
