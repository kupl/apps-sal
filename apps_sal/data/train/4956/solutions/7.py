def protein_synthesis(dna: str):
    RNA_DICT = {'A': 'U', 'G': 'C', 'C': 'G', 'T': 'A'}
    rna_strand = ''.join([RNA_DICT[base] for base in dna])
    rna = ' '.join([rna_strand[base:base + 3] for base in range(0, len(rna_strand), 3)])
    print(rna)
    length_rna = len(rna.split(' '))
    protein = [CODON_DICT.get(rna.split(' ')[codon_i], '') for codon_i in range(0, length_rna)]
    print(protein)
    protein = ' '.join([_f for _f in protein if _f])
    print(protein)
    return (rna, protein)
