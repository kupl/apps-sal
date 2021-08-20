def reverse_complement(dna):
    table = str.maketrans('ACGT', 'TGCA')
    return 'Invalid sequence' if set(dna) - set('ACGT') else dna.translate(table)[::-1]
