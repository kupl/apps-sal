def dna_to_rna(dna):
    res = ''
    for i in dna:
        if i == 'T':
            res += 'U'
        else:
            res += i
    return res
