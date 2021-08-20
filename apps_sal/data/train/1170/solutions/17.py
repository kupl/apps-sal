for _ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    res = ''
    for i in range(n):
        if arr[i] % k == 0:
            res = res + '1'
        else:
            res += '0'
    print(res)
