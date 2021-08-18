def dna_to_rna(dna):

    dna = dna.upper()

    if 'T' in dna:
        dnaList = list(dna)
        while 'T' in dnaList:
            dnaList[dnaList.index('T')] = 'U'
        rna = ''.join(dnaList)
    else:
        rna = dna

    return rna
