def dna_to_rna(dna):
    j = ""
    for i in dna:
        if i == "T":
            j += "U"
        else:
            j += i
    return j
