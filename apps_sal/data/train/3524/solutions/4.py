def dna_to_rna(mot):

    new_mot = [lettre.replace('T', 'U') for lettre in mot]
    return "".join(new_mot)
