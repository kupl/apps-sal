def dna_to_rna(dna):
    rna = ''
    for base in dna:
        if base == 'T':
            rna = rna + 'U'
        elif base == 'G' or 'C' or 'A':
            rna = rna + base
        else:
            print(f'{base} is not a DNA nucleotide base')
    return rna
