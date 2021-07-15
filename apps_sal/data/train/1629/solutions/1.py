from collections import Counter

def exchange_sort(s):
    a,b,c = (Counter(zip(*p)) for p in ((s,sorted(s)), (sorted(s),s), (s,s)))
    return sum(((a|b) + a + b - c - c - c).values()) // 6
