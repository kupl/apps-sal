from itertools import permutations


def find_mult_3(num):
    ls = []
    for i in range(1, len(str(num)) + 1):
        for j in set(permutations(str(num), i)):
            ls.append(int(''.join(j)))
    ls = set(ls)
    solve = [x for x in ls if x != 0 and x % 3 == 0]
    return [len(solve), max(solve)]
