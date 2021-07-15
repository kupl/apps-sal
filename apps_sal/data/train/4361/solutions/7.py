from itertools import permutations, count

def next_perfectsq_perm(lower_limit, k):
    for i in count(int(lower_limit ** 0.5) + 1):
        j = i ** 2
        if '0' in str(j):
            continue
        k_count = 0
        matches = [j]
        perms = set(permutations(str(j))) - set(matches)
        for p in perms:
            num = int(''.join(p))
            if int(num ** 0.5) ** 2 == num:
                matches.append(num)
                k_count += 1
        if k_count == k:
            return sorted(matches)[-1]
