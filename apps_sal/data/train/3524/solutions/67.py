def dna_to_rna(dna):
    return "".join("U" if char == "T" else char for char in dna)
