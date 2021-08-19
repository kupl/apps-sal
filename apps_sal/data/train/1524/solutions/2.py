t = int(input())
for i in range(0, t):
    n = input().split(' ')
    n1 = int(n[0])
    k = int(n[1])
    ax = pow(k - 1, n1 - 1, 1000000007)
    ax = ax % 1000000007 * (k % 1000000007) % 1000000007
    print(ax)
