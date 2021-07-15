from itertools import zip_longest

tbl = str.maketrans("TAGC", "AUCG")


def protein_synthesis(dna: str):
    codons = [
        "".join(xs) for xs in zip_longest(*[iter(dna.translate(tbl))] * 3, fillvalue="")
    ]
    rna = " ".join(codons)
    protein = " ".join(CODON_DICT[codon] for codon in codons if codon in CODON_DICT)
    return rna, protein
