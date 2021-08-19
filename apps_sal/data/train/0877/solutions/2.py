t = int(input())
for j in range(t):
    (x, y, K, N) = list(map(int, input().split(' ')))
    val = abs(x - y)
    if val % K == 0:
        if val / K % 2 == 0:
            print('Yes')
        else:
            print('No')
    else:
        print('No')
