def dna_to_rna(dna):
    output = ''
    for i in dna:
        if i == 'T':
            output += 'U'
        else:
            output += i
    return output
