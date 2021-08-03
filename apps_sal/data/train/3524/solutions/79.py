#! python3

import re
dnaRegex = re.compile(r'T')


def dna_to_rna(dna):
    return dnaRegex.sub('U', dna)
