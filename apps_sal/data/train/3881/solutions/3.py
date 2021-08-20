import re
rnaDict = "Phenylalanine (F): UUU, UUC\nLeucine (L): UUA, UUG, CUU, CUC, CUA, CUG\nIsoleucine (I): AUU, AUC, AUA\nMethionine (M): AUG\nValine (V): GUU, GUC, GUA, GUG\nSerine (S): UCU, UCC, UCA, UCG, AGU, AGC\nProline (P): CCU, CCC, CCA, CCG\nThreonine (T): ACU, ACC, ACA, ACG\nAlanine(A): GCU, GCC, GCA, GCG\nTyrosine (Y): UAU, UAC\nHistidine (H): CAU, CAC\nGlutamine (Q): CAA, CAG\nAsparagine (N): AAU, AAC\nLysine (K): AAA, AAG\nAspartic Acid (D): GAU, GAC\nGlutamic Acid (E): GAA, GAG\nCysteine (C): UGU, UGC\nTryptophan (W): UGG\nArtinine (R): CGU, CGC, CGA, CGG, AGA, AGG\nGlycine (G): GGU, GGC, GGA, GGG\nStop Codon ('Stop'): UGA, UAA, UAG"


def protein(rna):
    transDict = {}
    for line in rnaDict.split('\n'):
        for section in line[line.index(':') + 1:].replace(' ', '').split(','):
            transDict[section] = re.findall("\\(+\\'?(\\w+)", line)[0]
    codec = ''
    while len(rna) > 0:
        if transDict[rna[:3]] == 'Stop':
            pass
        else:
            codec += transDict[rna[:3]]
        rna = rna[3:]
    return codec
