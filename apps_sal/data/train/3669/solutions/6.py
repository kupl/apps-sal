import itertools
def sc_perm_comb(num):
    line = []
    for i in range(len(str(num))):
        line += [int(''.join(n)) for n in itertools.permutations(list(str(num)), i+1)]
    return sum(set(line))

