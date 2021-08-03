def scf(arr):
    print(arr)
    if arr == []:
        return 1
    ret = []
    for j in arr:
        for i in range(1, int(j**0.5) + 1):
            if j % i == 0:
                ret.append(i)
                ret.append(j // i)
    if len(ret) == len(arr) * 2:
        return 1
    print(ret)
    ret1 = []
    for k in set(ret):
        if ret.count(k) >= len(arr) and k != 1:
            ret1.append(k)
    if ret1 == []:
        return 1
    else:
        return min(ret1)
