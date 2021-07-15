def protein_synthesis(dna):
    
    # Transcribe
    dna_to_rna = {'G': 'C', 
                  'C': 'G',
                  'A': 'U',
                  'T': 'A'}
    rna = ''
    counter = 1
    for acid in dna:
        rna += dna_to_rna[acid]
        if counter % 3 == 0:
            rna += ' '
        counter += 1
    
    # Translate
    protein = ''
    for codon in rna.split(' '):
        amac = CODON_DICT.get(codon, None)
        if amac is not None:
            protein += (amac + ' ')
    
    return (rna.strip(), protein.strip())
