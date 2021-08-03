d = 1000000007
for _ in range(int(input())):
    l = sorted(list(map(int, input().split())))
    ans = (l[0] % d) * ((l[1] - 1) % d) * ((l[2] - 2) % d)
    print(ans % d)
