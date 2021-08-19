import re
dnaRegex = re.compile('T')


def dna_to_rna(dna):
    return dnaRegex.sub('U', dna)
