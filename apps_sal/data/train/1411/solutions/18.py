
for _ in range(int(input())):
    x, r, a, b = map(int, input().split())
    c = max(a, b)
    ans = x * abs(b - a)
    if ans % c == 0:
        print(ans // c - 1)
    else:
        print(ans // c)
