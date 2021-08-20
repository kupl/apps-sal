t = int(input())
for i in range(t):
    (n, d) = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    r1 = []
    for j in arr:
        if j <= 9 or j >= 80:
            r1.append(j)
    for j in r1:
        arr.remove(j)
    t = len(r1) // d
    if t != len(r1) / d:
        t = t + 1
    n_t = len(arr) // d
    if n_t != len(arr) / d:
        n_t = n_t + 1
    print(n_t + t)
