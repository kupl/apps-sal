def solve(st):
    prefixes = set()
    sufixes = set()
    pref = ''
    suff = st[1:]
    for i in st[:-1]:
        sufixes.add(suff)
        suff = suff[1:]
        pref += i
        prefixes.add(pref)
    for i in sorted(sufixes.intersection(prefixes))[::-1]:
        if len(i) * 2 <= len(st):
            return len(i)
    return 0
