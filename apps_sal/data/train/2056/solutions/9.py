def solve(a, b):
    (i, n) = (0, len(a))
    res = 0
    while i < n:
        if a[i] == b[i]:
            i += 1
            continue
        res += 1
        if i < n - 1 and a[i + 1] != b[i + 1] and (a[i] != a[i + 1]):
            i += 2
        else:
            i += 1
    return res


input()
a = input().strip()
b = input().strip()
print(solve(a, b))
