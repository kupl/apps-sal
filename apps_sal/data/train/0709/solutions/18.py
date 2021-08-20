for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(max(a[0], a[n - 1]))
