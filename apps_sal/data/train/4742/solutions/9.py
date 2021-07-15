def duplicates(arr):
    seen, count = set(), 0
    for n in arr:
        if n in seen:
            seen.remove(n)
            count += 1
        else:
            seen.add(n)
    return count
