for _ in range(int(input())):
    n, m, s = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    count = 0
    arr2.sort()
    arr3 = arr2.copy()
    count2 = 0
    for k in arr3:
        if k > s * 2:
            arr2.remove(k)
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
