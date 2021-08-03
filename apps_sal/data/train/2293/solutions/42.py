N = int(input())
A = list(map(int, input().split()))

data = [[(A[0], 0), (-1, -1)] for i in range(2**N)]
for i in range(1, 2**N):
    for j in range(N):
        if i >> j & 1 == 1:
            a, b = data[i - 2**j]
            if a[0] > data[i][0][0]:
                data[i][1] = data[i][0]
                data[i][0] = a
            elif a[0] > data[i][1][0] and a[1] != data[i][0][1]:
                data[i][1] = a
            if b[0] > data[i][0][0]:
                data[i][1] = data[i][0]
                data[i][0] = b
            elif b[0] > data[i][1][0] and b[1] != data[i][0][1]:
                data[i][1] = b
    a = (A[i], i)
    if a[0] > data[i][0][0]:
        data[i][1] = data[i][0]
        data[i][0] = a
    elif a[0] > data[i][1][0] and a[1] != data[i][0][1]:
        data[i][1] = a


ans = [data[i][0][0] + data[i][1][0] for i in range(2**N)]
for i in range(2, 2**N):
    ans[i] = max(ans[i], ans[i - 1])

for i in range(1, 2**N):
    print((ans[i]))
