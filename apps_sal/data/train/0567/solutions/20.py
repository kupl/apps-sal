for _ in range(int(input())):
    a = int(input())
    arr = list(map(int, input().split()))
    prev = arr[0]
    count = 0
    f = 0
    for i in arr:
        if i == prev:
            count += 1
        else:
            prev = i
            count = 1
        if count >= 3:
            print('Yes')
            f = 1
            break
    if not f:
        print('No')
