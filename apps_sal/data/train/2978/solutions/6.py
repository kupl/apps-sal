from collections import Counter, defaultdict


def count_sel(lst):
    c = Counter(lst)
    freq = defaultdict(list)
    for (n, v) in c.items():
        freq[v].append(n)
    (maxF, fLst) = max(freq.items(), default=(0, []))
    return [len(lst), len(c), len(freq[1]), [sorted(fLst), maxF]]
