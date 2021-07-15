MRNA_TABLE = str.maketrans("ACGT", "UGCA")

def protein_synthesis(dna):
    rna = dna.translate(MRNA_TABLE)
    codons = [rna[i:i+3] for i in range(0, len(rna), 3)]
    return " ".join(codons), " ".join(CODON_DICT[codon] for codon in codons if codon in CODON_DICT)

