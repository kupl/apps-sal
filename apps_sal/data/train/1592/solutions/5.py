t = int(input())
for i in range(t):
    n = int(input())
    chef = 0
    t = []
    for i in range(n):
        l = list(map(int, input().split()))
        c = l[0]
        if c % 2 == 0:
            for i in range(1, len(l) // 2 + 1):
                chef = chef + l[i]
            continue
        for i in range(1, len(l) // 2):
            chef = chef + l[i]
        t.append(l[len(l) // 2])
    t.sort(reverse=True)
    for i in range(len(t)):
        if i % 2 == 0:
            chef = chef + t[i]
    print(chef)
