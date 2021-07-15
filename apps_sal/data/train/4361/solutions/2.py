from itertools import permutations
def next_perfectsq_perm(lower_limit, k): 
    while 1:
        lower_limit += 1
        if '0' not in str(lower_limit) and int(lower_limit ** 0.5 + 0.5) ** 2 == lower_limit:
            perms = list([''.join(x) for x in set(permutations(str(lower_limit)))])
            perms = list(map(int, perms))
            perfects = 0
            perfect_list = []
            for i in perms:
                if int(i ** 0.5 + 0.5) ** 2 == i:
                    perfects += 1
                    perfect_list.append(i)
            if perfects == k:
                return max(perfect_list)   

