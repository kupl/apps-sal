def dna_to_rna(dna):
    
    ret = "";
    print(dna)
    for c in dna:
        if c == 'T':
            ret = ret + "U"
        else:
            ret = ret + c
        
    print(ret)
    return ret
