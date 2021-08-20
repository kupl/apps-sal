M = 10 ** 9 + 7
for _ in range(int(input())):
    (x, y, s) = [int(s) for s in input().split()]
    (u, v) = [int(s) for s in input().split()]
    if s % x == 0 and s // x & s // x - 1 == 0:
        w = s // x
    else:
        w = s // y
        u = v - u
    ans = w % M * (v % M) % M * pow(u, M - 2, M) % M
    print(ans)
