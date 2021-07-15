def dna_to_rna(dna):
    s=""
    for i in dna:
        if(i=="T"):
            i="U"
            s=s+i
        else:
            s=s+i
    return s
