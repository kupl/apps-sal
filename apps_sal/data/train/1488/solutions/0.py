from itertools import permutations
for _ in range(int(input())):
    (N, K) = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    arr1 = []
    arr2 = []
    for i in range(1, len(arr) + 1):
        arr1.append(i)
    indexzero = []
    for i in range(0, len(arr)):
        if arr[i] == 0:
            indexzero.append(i)
        else:
            arr2.append(arr[i])
    arr3 = list(set(arr1) - set(arr2))
    result = permutations(arr3)
    perm = []
    for i in result:
        perm.append(i)
    step = 0
    count = 0
    for p in range(0, len(perm)):
        temp = []
        for q in range(0, len(arr)):
            if arr[q] == 0:
                temp.append(perm[p][step])
                step += 1
            else:
                temp.append(arr[q])
        k = 0
        step = 0
        for m in range(0, len(temp) - 1):
            if temp[m] < temp[m + 1]:
                k += 1
        if k == K:
            count += 1
    print(count)
