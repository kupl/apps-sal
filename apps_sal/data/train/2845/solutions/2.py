trans = str.maketrans("ATCG", "TAGC")


def check_DNA(seq1, seq2):
    seq1, seq2 = sorted((seq1, seq2), key=len)
    return seq1[::-1].translate(trans) in seq2
