def dna_to_rna(dna):
    output = []
    for i in dna:
        if i == 'T':
            output.append('U')
        else: 
            output.append(i)
    return ''.join(output)
