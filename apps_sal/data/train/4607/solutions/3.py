from itertools import combinations, permutations

def find_mult_3(num):
    n = [int(c) for c in str(num)]
    r = set()
    for i in range(1, len(n)+1):
        for c in combinations(n, i):
            if sum(c) % 3 == 0:
                r |= set([int(''.join([str(i) for i in p])) for p in permutations(c) if p[0] != 0])
    
    return [len(r), max(r)]
