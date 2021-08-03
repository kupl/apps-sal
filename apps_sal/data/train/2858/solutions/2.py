def to_bin(comb):
    s = ''.join(('1' if d == '*' else '0' for d in comb))
    return (int(s, 2))


def shifter(comb1, comb2):
    b1, b2 = to_bin(comb1), to_bin(comb2)
    sh = 0
    while b1 & (b2 << sh):
        sh += 1
    return max(len(comb1), len(comb2) + sh)


def combs(comb1, comb2):
    return min(shifter(comb1, comb2), shifter(comb2, comb1))
