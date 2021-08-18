t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(lambda x: int(x), input().split()))
    b = []
    for i in range(0, len(a)):
        b.append((a[i], i))
    b.sort(key=lambda x: x[0])
    hashmap = {}
    maximum = 0
    for i in range(0, len(a)):
        if a[i] not in hashmap:
            hashmap[a[i]] = 0
        hashmap[a[i]] += 1
        if hashmap[a[i]] > maximum:
            maximum = hashmap[a[i]]
    if maximum > n - maximum:
        print("No")
    else:
        print("Yes")
        c = []
        for i in range(0, len(b)):
            c.append(b[(i + maximum) % n])
        d = [0 for _ in range(n)]
        for i in range(0, len(b)):
            d[b[i][1]] = c[i][0]
        for i in d:
            print(i, end=" ")
        print()
