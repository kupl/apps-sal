def dna_to_rna(dna):
    
    rna = ""
    
    for ch in dna:
        if ch =="T":
            rna += "U"
        else:
            rna += ch
    
    return rna
