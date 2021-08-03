def protein_synthesis(dna):
    rna = ""
    protein = ""
    for i in range(len(dna)):
        if i % 3 == 0 and i != 0:
            rna += " "
        if dna[i] == "C":
            rna += "G"
        elif dna[i] == "G":
            rna += "C"
        elif dna[i] == "T":
            rna += "A"
        elif dna[i] == "A":
            rna += "U"
    rna_list = rna.split(" ")
    for element in rna_list:
        if len(element) == 3:
            protein += CODON_DICT[element] + " "
    return (rna, protein.strip())
