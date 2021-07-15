from collections import Counter

def common(a,b,c):
    counts_a, counts_b, counts_c = Counter(a), Counter(b), Counter(c)
    sum = 0
    for n in (set(counts_a.keys()) & set(counts_b.keys())) & set(counts_c.keys()):
        sum += n * min([counts_a[n], counts_b[n], counts_c[n]])
    return sum
