
for __ in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    s = set(arr)
    mex = -1
    ele = 1
    for i in range(1, n + 1):
        if i not in s:
            mex = i
            break
    if m > mex:
        print(-1)
    elif m == mex:
        print(n)
    else:
        c = arr.count(m)
        print(n - c)
