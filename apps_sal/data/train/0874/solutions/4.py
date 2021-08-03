for _ in range(int(input())):
    n, m, s = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    count = 0
    arr2.sort()
    j = n
    arr3 = arr2.copy()
    count2 = 0
    for k in range(len(arr3)):
        if arr3[k] > s * 2:
            j = k
            break
    arr2 = arr2[:j]
    for kk in arr2:
        if count >= m:
            break
        elif kk <= s:
            count += 1
            count2 += 1
        else:
            count += 2
            count2 += 1
    if count <= m:
        print(count2)
    else:
        print(count2 - 1)
