def solve(n):
    s = [0, 1][len(n) % 2]
    lh = n[:len(n) // 2]
    hh = n[len(n) // 2 + s:]
    if s and lh == hh[::-1]:
        return True
    diffs = 0
    for u, v in zip(lh, hh[::-1]):
        if u != v:
            diffs += 1
        if diffs > 1:
            return False
    return diffs == 1
