from itertools import combinations


def longest_comb(arr, command):
    reverse = True if command[0] == '>' else False
    if arr == sorted(arr, reverse=reverse) and len(arr) == len(set(arr)):
        return arr
    n = len(arr) - 1
    while(n > 2):
        r = []
        for c in combinations(range(0, len(arr)), n):
            a = [arr[i] for i in c]
            if a == sorted(a, reverse=reverse) and len(a) == len(set(a)):
                r.append(a)
        if len(r) == 1:
            return r[0]
        elif len(r) > 1:
            return r
        n -= 1
    return []
