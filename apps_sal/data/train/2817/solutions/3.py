def DNA_strand(dna):
    dnaComplement = ''
    for string in dna:
        if string == 'A':
            dnaComplement += 'T'
        elif string == 'T':
            dnaComplement += 'A'
        elif string == 'G':
            dnaComplement += 'C'
        elif string == 'C':
            dnaComplement += 'G'
    return dnaComplement
