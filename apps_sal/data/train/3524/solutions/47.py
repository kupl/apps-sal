def dna_to_rna(dna):
    import re
    return re.sub(r"T", "U", dna)
