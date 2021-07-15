from itertools import permutations

def find_mult_3(num):
    num_list = tuple(map(int, str(num)))
    
    poss = set()
    for i in range(1, len(num_list)+1):
        poss |= set(permutations(num_list, i))
    
    res = set()
    for p in poss:
        if p[0] != 0 and sum(p) % 3 == 0:
            res.add(p)

    res = [sum(x * 10**n for n, x in enumerate(p[::-1])) for p in res]
    return [len(res), max(res)]

