t = int(input())
for r in range(t):
    n = int(input())
    s = input()
    a = list(map(int, s.split()))
    a.sort()
    p = a[0]
    for j in range(1, n):
        p = p % a[j]
    print(p)
