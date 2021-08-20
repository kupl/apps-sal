line = input().split()
N = int(line[0])
K = int(line[1])
b = list(map(int, input().split()))
i = 0
if K == 0:
    print(' '.join((str(x) for x in b)))
else:
    mx = max(b)
    for j in range(0, N):
        b[j] = mx - b[j]
    if K % 2 == 0:
        mx = max(b)
        for j in range(0, N):
            b[j] = mx - b[j]
        print(' '.join((str(x) for x in b)))
    else:
        print(' '.join((str(x) for x in b)))
