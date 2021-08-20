def dna_to_rna(dna):
    dnaList = list(dna)
    rnaList = []
    for x in dnaList:
        if x == 'T':
            rnaList.append('U')
        else:
            rnaList.append(x)
    return ''.join(rnaList)
