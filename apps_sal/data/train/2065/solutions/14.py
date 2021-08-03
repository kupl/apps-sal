n, k = (int(x) for x in input().split())
l = [None for _ in range(k)]
for i in range(k):
    l[i] = [int(x) for x in input().split()[1:]]
for m in l:
    if m[0] == 1:
        i = 0
        while i < len(m) and m[i] == i + 1:
            i += 1
        print(n * 2 - i * 2 - k + 1)
