def mystery_range(s, n):
    for i in range(1, 100):
        if sorted(list(s)) == sorted(list(''.join(str(x) for x in list(range(i, i + n))))) and str(i) in s:
            return [i, i + n - 1]
