def dna_to_rna(dna):
    res = ""
    if(len(dna) == 0):
        return res
    else:
        for item in dna:
            if(item == "T"):
                res += "U"
            else:
                res += item
        return res
