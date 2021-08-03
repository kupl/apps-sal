def position(alphabet):
    alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    n = 0
    for i in range(0, 26):
        if alp[i] == alphabet:
            a = int(alp.index(alp[i])) + 1
    return "Position of alphabet: {}".format(a)
