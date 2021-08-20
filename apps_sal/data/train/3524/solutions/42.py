def dna_to_rna(dna):
    rna = ''
    for letter in dna:
        if letter == 'T':
            rna += 'U'
        else:
            rna += letter
    return rna
