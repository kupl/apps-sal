def automorphic(n):
    end_n = str(n)
    sq = n * n
    end_sq = str(sq)
    end_sq = end_sq[len(end_sq) - len(end_n):]
    if (end_n == end_sq):
        return ('Automorphic')
    return ('Not!!')
