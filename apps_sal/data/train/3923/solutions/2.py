from collections import Counter

def micro_world(bacteria, k):
    L = sorted(Counter(bacteria).items())
    return sum(v1 for (k1,v1),(k2,_) in zip(L, L[1:]) if k2 > k1+k) + L[-1][1]
