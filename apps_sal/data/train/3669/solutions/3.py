import itertools


def sc_perm_comb(num):
    total = 0
    for k in range(1, len(str(num)) + 1):
        t = set((itertools.permutations(str(num), k)))
        for l in t:
            temp = ''.join(l)
            if(temp[0:1] != '0'):
                total += int(temp)
    return total
