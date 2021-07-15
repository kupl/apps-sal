def reverse_complement(dna):
    dna = dna[::-1]
    table = dna.maketrans('ATCG', 'TAGC')
    symbols = 'ACTG'
    for i in dna:
        if i not in symbols:
            return 'Invalid sequence'
    return dna.translate(table)

