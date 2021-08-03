def dna_to_rna(dna):
    dna_bases = []
    for item in dna:
        dna_bases.append(str(item))
    rna_lst = []
    for item in dna_bases:
        if item == 'A' or item == 'C' or item == 'G':
            rna_lst.append(item)
        elif item == 'T':
            rna_lst.append('U')
        else:
            print("This is no dna structure")
            break
    rna = ''.join(rna_lst)
    return rna
