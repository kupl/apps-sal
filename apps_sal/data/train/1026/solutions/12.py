
mo = 1000000007

for _ in range(int(input())):
    l = list(map(int, input().split()))
    l.sort()
    print((l[0] * ((l[1] - 1) % mo) * ((l[2] - 2) % mo)) % mo)
