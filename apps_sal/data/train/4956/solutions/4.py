def protein_synthesis(dna):
    # Transcribe
    DNA2RNA = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}     # Dictionary for conversion to RNA
    rnaList = [DNA2RNA[i] for i in dna]  # Transcribe to RNA

    # Translate
    # Note: A pre-loaded CODON_DICT exists that takes 3-letter RNA keys and outputs amino acid names.
    aa = []  # list to hold aa names
    for i in range(0, len(rnaList) - 2, 3):
        aa.append(CODON_DICT[''.join(rnaList[i:i + 3])])

    # Convert RNA to output format
    mRNA = [''.join(rnaList[i:i + 3]) for i in range(0, len(rnaList), 3)]

    return (" ".join(mRNA), " ".join(aa))
