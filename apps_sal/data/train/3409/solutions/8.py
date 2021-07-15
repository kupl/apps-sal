from collections import Counter

def fish(shoal):
    c = Counter(map(int, shoal.replace('0', '')))
    consumed = 0
    for size in range(1, 99999):
        consumed += size * c[size]
        if consumed < size * (size+1) * 2:
            return size
