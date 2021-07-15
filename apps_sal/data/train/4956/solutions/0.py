import re

TABLE = str.maketrans('ACGT','UGCA')

def protein_synthesis(dna):
    rna = re.findall(r'.{1,3}', dna.translate(TABLE))
    return ' '.join(rna), ' '.join(x for x in map(CODON_DICT.get, rna) if x)
