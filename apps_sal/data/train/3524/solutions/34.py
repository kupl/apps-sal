def dna_to_rna(dna):
    result = ''
    for i in dna:
        if i == 'T' or '':
            i = 'U'
        result += i
    return result


print(dna_to_rna('GCAT'))
