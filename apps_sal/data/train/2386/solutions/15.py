t = int(input())
for _ in range(t):
    n = int(input())
    v = list(map(int, input().split()))
    tmp = []
    for i in v:
        if i not in tmp:
            tmp.append(i)
    for i in tmp:
        print(i, end=' ')
    print()
