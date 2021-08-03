t = int(input())
for i in range(t):
    x, y, K, N = list(map(int, input().split()))

    if (abs(x - y) % (2 * K) == 0):
        print('Yes')
    else:
        print('No')
