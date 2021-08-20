def twos_difference(lst):
    (results, memo) = ([], {})
    for n in lst:
        if n in memo:
            for k in memo[n]:
                (a, b) = sorted([k, n])
                results.append((a, b))
        memo.setdefault(n + 2, []).append(n)
        memo.setdefault(n - 2, []).append(n)
    return sorted(results)
