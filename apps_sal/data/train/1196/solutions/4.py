import numpy as np


def s(arr, n, m, k):
    max_sum = 0
    for i in range(n):
        prev_sum = 0
        curr_sum = 0
        for a in range(k):
            curr_sum += arr[i][a]
        prev_sum = curr_sum
        if max_sum < prev_sum:
            max_sum = prev_sum
        j = 1
        while j + k <= m:
            curr_sum = prev_sum - arr[i][j - 1] + arr[i][j + k - 1]
            prev_sum = curr_sum
            if max_sum < prev_sum:
                max_sum = prev_sum
            j += 1
    return max_sum


for _ in range(int(input())):
    (n, m, k) = list(map(int, input().split()))
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    ans = s(arr, n, m, k)
    arr = np.array(arr)
    arr = arr.T
    l = []
    for i in range(m):
        l.append(list(arr[i]))
    temp = s(l, m, n, k)
    if ans < temp:
        ans = temp
    print(ans)
