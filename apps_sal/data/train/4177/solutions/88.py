def men_from_boys(arr):
    m = list(set([i for i in arr if i % 2 == 0]))
    m.sort()
    n = list(set([i for i in arr if i % 2]))
    n.sort(reverse=True)
    return m + n
