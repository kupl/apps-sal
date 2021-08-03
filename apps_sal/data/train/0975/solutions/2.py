for _ in range(int(input())):
    count = 0
    nc = 0
    arr1 = []
    arr2 = []
    n, r, x, y = list(map(int, input().split()))
    if x != 0:
        arr1 = list(map(int, input().split()))
    if y != 0:
        arr2 = list(map(int, input().split()))
    zz = len(set(arr1).union(set(arr2)))
    n -= zz
    if n >= r:
        print(r)
    else:
        print(n)
