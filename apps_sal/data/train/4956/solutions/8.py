def protein_synthesis(dna):
    # Transcribe
    s = dna.translate(str.maketrans('TAGC', 'AUCG'))
    rna = [s[i:i + 3] for i in range(0, len(s), 3)]
    # Translate
    # Note: A pre-loaded CODON_DICT exists that takes 3-letter RNA keys and outputs amino acid names.
    protein = [CODON_DICT[r] for r in rna if r in CODON_DICT]
    return (' '.join(rna), ' '.join(protein))
