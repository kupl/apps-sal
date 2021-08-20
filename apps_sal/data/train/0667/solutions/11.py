for _ in range(int(input())):
    (n, d) = map(int, input().split())
    arr = list(map(int, input().split()))
    for i in range(n):
        item = arr[n - 1 - i]
        d = d // item * item
    print(d)
