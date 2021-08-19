def code_for_same_protein(seq1, seq2):
    if seq1 == seq2:
        return True
    lista = [['GCT', 'GCC', 'GCA', 'GCG'], ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'], ['AAT', 'AAC'], ['GAT', 'GAC'], ['AAT', 'AAC', 'GAT', 'GAC'], ['TGT', 'TGC'], ['CAA', 'CAG'], ['GAA', 'GAG'], ['CAA', 'CAG', 'GAA', 'GAG'], ['GGT', 'GGC', 'GGA', 'GGG'], ['CAT', 'CAC'], ['ATG'], ['ATT', 'ATC', 'ATA'], ['CTT', 'CTC', 'CTA', 'CTG', 'TTA', 'TTG'], ['AAA', 'AAG'], ['ATG'], ['TTT', 'TTC'], ['CCT', 'CCC', 'CCA', 'CCG'], ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'], ['ACT', 'ACC', 'ACA', 'ACG'], ['TGG'], ['TAT', 'TAC'], ['GTT', 'GTC', 'GTA', 'GTG'], ['TAA', 'TGA', 'TAG']]
    for j in range(0, len(lista)):
        for i in range(0, len(seq1), 3):
            if seq1[i:i + 3] in lista[j] and seq2[i:i + 3] not in lista[j]:
                return False
    return True
