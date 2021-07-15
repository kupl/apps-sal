def find_dups_miss(arr):
    min_n, max_n = min(arr), max(arr)
    seen, dupes = set(), set()
    
    for n in arr:
        if n in seen:
            dupes.add(n)
        else:
            seen.add(n)
    
    missing = (min_n + max_n) / 2.0 * (max_n - min_n + 1) - sum(seen)
    return [ missing, sorted(dupes) ]
