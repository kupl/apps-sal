t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    freq = {}
    freq[arr[0]] = 1
    flag = 0
    for i in range(1, n):
        if arr[i - 1] != arr[i] and arr[i] in freq:
            flag = 1
            break
        if arr[i] in freq:
            freq[arr[i]] += 1
        else:
            freq[arr[i]] = 1
    sam = []
    for i in freq:
        sam.append(freq[i])
    sam2 = list(set(sam))
    sam.sort()
    sam2.sort()
    if sam != sam2:
        flag = 1
    if flag == 1:
        print('NO')
    else:
        print('YES')
