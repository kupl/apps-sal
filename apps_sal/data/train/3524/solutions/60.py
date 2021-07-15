def dna_to_rna(dna):
    rna = ''
    for i in dna:
        if i.upper() == 'T':
            rna += 'U'
        else:
            rna += i.upper()
    return rna
