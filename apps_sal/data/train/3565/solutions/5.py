from collections import defaultdict


def solve(st, k):
    (D, current, removed) = (defaultdict(list), ord('a'), set())
    for (i, c) in enumerate(st):
        D[ord(c)].append(i)
    while k and len(removed) < len(st):
        removed |= set(D[current][:k])
        k -= min(k, len(D[current]))
        current += 1
    return ''.join((c for (i, c) in enumerate(st) if i not in removed))
