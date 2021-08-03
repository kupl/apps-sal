for z in range(eval(input())):
    n = eval(input())
    arr = list(map(int, input().split()))
    c = 0
    i = 1
    s = arr[0]
    while i <= n:
        if arr[i] > s:
            c += 1
        i += 1
    print(c)
