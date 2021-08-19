t = int(input())
for _ in range(t):
    (n, k) = map(int, input().split())
    old = input().split()
    a = [input() for i in range(k)]
    d = {}
    for j in old:
        d[j] = 'NO'
    for i in old:
        for j in a:
            if d.get(i) == 'NO':
                if i in j:
                    d[i] = 'YES'
    b = [i for i in d.values()]
    print(*b)
