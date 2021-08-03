import sys

while(1):

    n = int(sys.stdin.readline().strip())
    if (n == 0):
        return

    a = list(map(int, input().split()))

    for i in range((2**(n - 1)) - 2, -1, -1):
        a[i] = max(a[i] * a[2 * (i + 1) - 1], a[i] * a[2 * i + 2])
    print(a[0] % 1000000007)
