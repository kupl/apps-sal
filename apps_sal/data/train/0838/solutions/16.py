t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    m = l[0]
    index = 0
    for i in range(len(l) - 1, -1, -1):
        if l[i] + i > m:
            index = i
            m = l[i] + i
    print(m)
