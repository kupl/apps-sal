def dna_to_rna(dna):
    result = []
    for x in dna:
        if x == 'T':
            result.append('U')
        else:
            result.append(x)
    return ''.join(result)
