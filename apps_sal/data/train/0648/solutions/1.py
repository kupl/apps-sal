def find_pos(arr, n, p, c):
    i = p
    i1 = p
    while i <= n and c > 0:
        if arr[i1] < arr[i]:
            if i - i1 > 100:
                return i1
            (c, i1) = (c - 1, i)
        i += 1
    return i1


(n, q) = list(map(int, input().split()))
arr = [0] + list(map(int, input().split()))
for a0 in range(1, q + 1):
    temp = list(map(int, input().split()))
    if temp[0] == 1:
        (p, c) = (temp[1], temp[2])
        print(find_pos(arr, n, p, c))
    else:
        (l, r, val) = (temp[1], temp[2], temp[3])
        for i in range(l, r + 1):
            arr[i] += val
