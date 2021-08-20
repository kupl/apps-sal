def dna_to_rna(dna):
    results = []
    for x in dna:
        if x == 'T':
            results.append('U')
        else:
            results.append(x)
    return ''.join(results)
