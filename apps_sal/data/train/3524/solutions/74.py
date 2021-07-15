def dna_to_rna(dna):
    pattern1 = "GCAT"
    pattern2 = "GCAU"
    
    translation = str.maketrans(pattern1, pattern2)
    
    return dna.translate(translation)

