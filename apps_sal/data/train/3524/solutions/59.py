def dna_to_rna(s):
    s1 = ""
    for i in s:
        if(i == "T"):
            s1 += "U"
        elif(i == "U"):
            s1 += "T"
        else:
            s1 += i
    return s1
