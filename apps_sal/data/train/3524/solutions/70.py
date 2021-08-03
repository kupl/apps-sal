def dna_to_rna(dna):
    new = ""
    for i in dna:
        if i in ["G", "C", "A"]:
            new += i
        elif i == "T":
            new += "U"
    return new
