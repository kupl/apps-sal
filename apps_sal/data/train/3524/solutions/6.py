def dna_to_rna(dna):
    total = ""
    for i in dna:
        if i == "T":
            total += "U"
        else:
            total += i
    return total
