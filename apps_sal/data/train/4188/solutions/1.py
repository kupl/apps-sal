def find_dup(arr):
    seen = set()
    for a in arr:
        if a in seen:
            return a
        seen.add(a)

