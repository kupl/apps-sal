def array_equalization(a, k):
    min_ = float('inf')
    for x in set(a):
        count = 0
        i = 0
        while i < len(a):
            if a[i] != x:
                count += 1
                i += k
            else:
                i += 1
        min_ = min(count, min_)
    return min_
