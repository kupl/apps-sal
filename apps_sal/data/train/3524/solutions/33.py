def dna_to_rna(dna):
    new = ''
    for i in range(len(dna)):
        if dna[i]=='T':
            new+= 'U'
        else:
            new+= dna[i]
    return new

