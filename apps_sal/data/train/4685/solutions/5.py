def self_descriptive(num):
    from collections import Counter

    snum = str(num)
    c = Counter(snum)
    return all(int(d) == c[str(i)] for i, d in enumerate(snum))
