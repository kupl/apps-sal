def dna_to_rna(dna):
    rna = ""
    for c in dna:
        if c == 'T':
            rna += 'U'
        else:
            rna += c
    return rna
