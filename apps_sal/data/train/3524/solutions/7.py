def dna_to_rna(dna):
    res = ''
    for let in dna:
        if let == 'T':
            res += 'U'
        else:
            res += let
    return res
