def dna_to_rna(dna):
    if "T" in dna:
        return dna.replace("T", "U")
    else:
        return dna
