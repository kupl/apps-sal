for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = set(map(int, input().split()))
    brr = set(map(int, input().split()))
    a = arr ^ brr
    for i in a:
        print(i, end=' ')
