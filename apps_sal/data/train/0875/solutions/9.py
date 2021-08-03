def check(arr, z):
    for i in arr:
        if i in z:
            return 1
    for i in arr:
        flag = True
        for j in arr:
            if i + j in z or i - j in z:
                flag = False
                break
        if flag:
            return 0
    return 2


for test_case in range(int(input())):
    n, z1, z2 = [int(i) for i in input().split()]
    arr = [int(i) for i in input().split()]
    arr += [-i for i in arr]
    print(check(arr, (z1, z2)))
