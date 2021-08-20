def db_sort(arr):
    (n, s) = ([], [])
    for v in arr:
        if type(v).__name__ == 'str':
            s.append(v)
        else:
            n.append(v)
    return sorted(n) + sorted(s)
