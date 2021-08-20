def protein_synthesis(dna):
    DNA2RNA = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}
    rnaList = [DNA2RNA[i] for i in dna]
    aa = []
    for i in range(0, len(rnaList) - 2, 3):
        aa.append(CODON_DICT[''.join(rnaList[i:i + 3])])
    mRNA = [''.join(rnaList[i:i + 3]) for i in range(0, len(rnaList), 3)]
    return (' '.join(mRNA), ' '.join(aa))
