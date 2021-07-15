def protein_synthesis(dna):
    
    # Transcribe
    table = str.maketrans('GCAT', 'CGUA')
    pressed_rna = dna.translate(table)

    rna = []
    for bit in range(0, len(pressed_rna)):
        if bit % 3 == 0:
            rna.append(' ')         
        rna.append(pressed_rna[bit])
         
    rna = ''.join(rna).strip()
    
    # Translate
    protein = []
    for rna_bit in rna.split(' '):
        protein_bit = CODON_DICT.get(rna_bit, None)
        if protein_bit is not None:
            protein.append(protein_bit)
    
    protein = ' '.join(protein)
    
    return rna, protein
