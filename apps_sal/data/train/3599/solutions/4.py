from itertools import count

def find_f1_eq_f2(n, k):
    digits = set(map(str, range(k)))
    for n in count(n + 1):
        for m in map(set, map(str, count(n, n))):
            if m <= digits:
                if len(m) == len(digits): return n
                break
