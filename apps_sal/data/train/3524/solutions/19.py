dnatab = 'T'
rnatab = 'U'


def dna_to_rna(dna):
    return dna.translate(dna.maketrans(dnatab, rnatab))
