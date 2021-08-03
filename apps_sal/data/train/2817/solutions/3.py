def DNA_strand(dna):
    # code here
    dnaComplement = ""
    for string in dna:
        if string == "A":
            dnaComplement += "T"
        elif string == "T":
            dnaComplement += "A"
        elif string == "G":
            dnaComplement += "C"
        elif string == "C":
            dnaComplement += "G"
    return dnaComplement
