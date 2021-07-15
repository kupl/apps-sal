def dna_to_rna(dna):
    a = [i if i != "T" else "U" for i in dna]
    return "".join(a)

