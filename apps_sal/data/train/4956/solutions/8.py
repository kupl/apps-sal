def protein_synthesis(dna):
    s = dna.translate(str.maketrans('TAGC', 'AUCG'))
    rna = [s[i:i + 3] for i in range(0, len(s), 3)]
    protein = [CODON_DICT[r] for r in rna if r in CODON_DICT]
    return (' '.join(rna), ' '.join(protein))
