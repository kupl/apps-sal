def dna_to_rna(dna):
    y = ""
    i = 0
    while i < len(dna):
        if dna[i] == "T":
            y = y + "U"
            i = i + 1
        else:
            y = y + dna[i]
            i = i + 1
    return y
