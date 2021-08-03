h = sorted(2**i * 3**j * 5**k for i in range(35) for j in range(25) for k in range(15))


def hamming(n):
    return h[n - 1]
