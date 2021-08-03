t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    odd = [0] * n
    if arr[0] % 2 == 1:
        odd[0] = 1
    for i in range(1, n):
        if arr[i] % 2 == 1:
            odd[i] = 1
        odd[i] += odd[i - 1]
    qu = int(input())
    for q in range(qu):
        l, r = map(int, input().split())
        l = l - 1
        r = r - 1
        flag = 0
        c = odd[r]
        if l > 0:
            c -= odd[l - 1]
        if c == (r - l + 1):
            print("ODD")
        else:
            print("EVEN")
