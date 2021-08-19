t = int(input())
for _ in range(t):
    size = int(input())
    li = list(map(int, input().split()))
    c = 0
    for i in li:
        if i >= len(li) / 2:
            c += 1
    print(c)
