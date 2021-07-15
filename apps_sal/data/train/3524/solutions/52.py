def dna_to_rna(dna):
    rna=''
    for i in dna:
        if i == 'T':
            rna+='U'
        else:
            rna+=i
    print(rna)
    return rna
