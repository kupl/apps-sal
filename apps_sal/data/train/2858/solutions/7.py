def passage(comb1, comb2):
    for i in range(len(comb1)):
        cover = 0
        for j, s in enumerate(comb1[i:]):
            if j == len(comb2):
                return len(comb1)
            if s == comb2[j] == "*":
                break
            cover += 1
        else:
            return len(comb1) + len(comb2) - cover
    return len(comb1 + comb2)


def combs(comb1, comb2):
    comb2, comb1 = sorted([comb1, comb2], key=lambda x: len(x))
    return min(passage(comb1, comb2), passage(comb1[::-1], comb2[::-1]))
