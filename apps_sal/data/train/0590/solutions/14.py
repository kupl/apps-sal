T = int(input())
for i in range(T):
    n, x, m = list(map(int, input().split()))
    l1 = [int(i) for i in input().split()]
    if x == 1:
        l1[0] = l1[0] % 1000000007
        print(l1[0])
    elif x == 2:
        m = m % 1000000007
        l1[0] = l1[0] % 1000000007
        l1[1] = (l1[1] % 1000000007 + l1[0] * m % 1000000007) % 1000000007
        print(l1[1])
