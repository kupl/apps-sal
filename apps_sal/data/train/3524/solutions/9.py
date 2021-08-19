def dna_to_rna(dna):
    rna_line = []
    dna_str = dna.upper()
    for a in dna_str:
        if a == 'T':
            rna_line.append('U')
        else:
            rna_line.append(a)
    result = ''.join(rna_line)
    return result
