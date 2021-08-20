for i in range(int(input())):
    (n, k) = input().split()
    n = int(n)
    k = int(k)
    arr = list(map(int, input().split()))
    a = 0
    b = 0
    count = 0
    ans = 0
    temp = -1
    w = 0
    index1 = index2 = None
    while b < n:
        if arr[b] > k:
            if count == 0:
                index1 = b
                count += 1
            elif arr[b] == arr[index1]:
                index1 = b
            else:
                index2 = b
                count += 1
        if count == 2:
            w = 1
            ans = max(ans, b - a)
            a = index1 + 1
            index1 = index2
            index2 = None
            count = 1
        b += 1
    if w == 0 and count == 1:
        print(n)
    else:
        print(ans)
