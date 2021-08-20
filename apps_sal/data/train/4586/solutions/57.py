def tv_remote(word):
    import numpy as np
    (i, j, s) = (0, 0, 0)
    remote = np.array([['a', 'b', 'c', 'd', 'e', '1', '2', '3'], ['f', 'g', 'h', 'i', 'j', '4', '5', '6'], ['k', 'l', 'm', 'n', 'o', '7', '8', '9'], ['p', 'q', 'r', 's', 't', '.', '@', '0'], ['u', 'v', 'w', 'x', 'y', 'z', '_', '/']])
    for char in word:
        s += abs(np.where(remote == char)[0][0] - i) + abs(np.where(remote == char)[1][0] - j) + 1
        i = np.where(remote == char)[0][0]
        j = np.where(remote == char)[1][0]
    return s
