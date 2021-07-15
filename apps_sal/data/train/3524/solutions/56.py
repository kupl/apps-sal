def dna_to_rna(dna):
    ans = ''
    for i in dna:
        if i == 'T':
            ans = ans + 'U'
        else:
            ans = ans + i
    return ans
