# cook your dish here
for _ in range(int(input())):
    n = int(input())
    d = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: []}
    l = []
    su = 0
    for i in range(n):
        p, s = list(map(int, input().split()))
        if p <= 8:
            d[p] = d[p] + [s]
    for j in d:
        if len(d[j]) != 0:
            su = su + max(d[j])
    print(su)
