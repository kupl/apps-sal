table = str.maketrans("ACGT", "TGCA")


def check_DNA(seq1, seq2):
    seq1, seq2 = sorted((seq1, seq2), key=len)
    return seq1 in seq2[::-1].translate(table)
