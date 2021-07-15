def dna_to_rna(dna):
    f = ""
    for i in range(len(dna)):
        if dna[i] == "T":
            f += "U"
        else:
            f += dna[i]
    return f
