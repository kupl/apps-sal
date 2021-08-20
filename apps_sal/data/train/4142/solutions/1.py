def solve(lst):
    (seen, result) = (set(), [])
    for (i, st1) in enumerate(lst):
        current = 0
        for (j, st2) in enumerate(lst[i + 1:], i + 1):
            if j not in seen and set(st1) == set(st2):
                current += j
                seen.add(j)
        if current:
            result.append(i + current)
    return sorted(result)
