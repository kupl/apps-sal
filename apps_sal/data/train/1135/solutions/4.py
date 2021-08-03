for _ in range(int(input())):
    a = input().split()
    n = int(a[0])
    k = int(a[1])
    print(n - k, end=" ")
    for i in range(1, n - k):
        print(i, end=" ")
    for i in range(n - k + 1, n + 1):
        print(i, end=" ")
