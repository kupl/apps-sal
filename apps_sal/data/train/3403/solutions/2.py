# Numpy?
# https://media.tenor.com/images/36c2be302f423c792ead1cca7018fe88/tenor.png
def reorder(N, M):
    L1 = list(range(N >> 1))
    L2 = list(range(N >> 1, N))
    R = M % (N >> 1)
    return [L1[-R:] + L1[:-R], L2[-R:] + L2[:-R]]
