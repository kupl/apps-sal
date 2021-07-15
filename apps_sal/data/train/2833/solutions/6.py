def sect_sort(a, s, l=None):
    if l:
        return a[:s] + sorted(a[s:s+l]) + a[s+l:]
    return a[:s] + sorted(a[s:])
