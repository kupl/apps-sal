for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    x = a[0]
    for j in range(1, n):
        x = a[j] ^ x
    print(x)
