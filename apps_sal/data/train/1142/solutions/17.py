
res = []
for _ in range(int(input())):
    n = int(input())
    res.append(n)
    res.sort(reverse=True)
    print(res.index(n) + 1)
