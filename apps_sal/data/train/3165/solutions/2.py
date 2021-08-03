# https://www.youtube.com/watch?v=_UtCli1SgjI

def toothpick(N):
    if N <= 0:
        return 0
    n = 1 << (N.bit_length() - 1)
    i = N - n

    return toothpick(n) + 2 * toothpick(i) + toothpick(i + 1) - 1 if i else (2 * n**2 + 1) / 3
