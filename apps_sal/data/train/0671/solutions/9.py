for _ in range(int(input())):
    (n, s) = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    marr = []
    narr = []
    for i in range(len(arr)):
        if arr2[i] == 0:
            marr.append(arr[i])
        else:
            narr.append(arr[i])
    if len(marr) > 0 and len(narr) > 0:
        if 100 - s >= min(marr) + min(narr):
            print('yes')
        else:
            print('no')
    else:
        print('no')
