def dna_to_rna(dna):
    for x in dna:
        if x == "T":
            y = dna.replace("T", "U")
            return y
    return dna
