def printo(arr):
    for i in range(len(arr)):
        print(arr[i], end=' ')
    print('')


(n, k) = (int(e) for e in input().strip().split())
arr = [int(e) for e in input().strip().split()]
flag = 0
if k == 0:
    printo(arr)
    flag = 1
if flag == 0:
    mx = max(arr)
    for i in range(n):
        arr[i] = mx - arr[i]
    if k % 2 == 1:
        printo(arr)
    else:
        mx = max(arr)
        for i in range(n):
            arr[i] = mx - arr[i]
        printo(arr)
