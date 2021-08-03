from itertools import count, permutations


def next_perfectsq_perm(limit_below, k):
    for n in count(int(limit_below**.5) + 1):
        s = str(n**2)
        if '0' not in s:
            sq_set = {x for x in (int(''.join(p)) for p in permutations(s)) if (x**.5).is_integer()}
            if len(sq_set) == k:
                return max(sq_set)
