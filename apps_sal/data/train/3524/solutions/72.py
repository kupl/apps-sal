import string

def dna_to_rna(dna):
    translation = {84:85}
    return dna.translate(translation)
