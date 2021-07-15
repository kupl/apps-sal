def dna_to_rna(dna):
    rna = ''
    for nucleic_acid in dna:
        if nucleic_acid == 'T':
            rna += 'U'
        else:
            rna += nucleic_acid
    return rna
