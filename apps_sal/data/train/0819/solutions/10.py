def rec(x, y):
    if x == 1 or y == 1:
        return True
    if x == 0 or y == 0:
        return False
    l = max(x, y)
    m = min(x, y)
    return rec(l % m, m)


t = int(input())
for _ in range(t):
    a, b = (int(x) for x in input().split())
    if rec(a, b):
        print("YES")
    else:
        print("NO")
