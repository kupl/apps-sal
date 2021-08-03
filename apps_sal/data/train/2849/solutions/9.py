def peak(arr):
    left_sum, right_sum = [0], [0]
    for n in arr:
        left_sum.append(n + left_sum[-1])
    for n in arr[::-1]:
        right_sum.append(n + right_sum[-1])
    for i in range(len(arr)):
        if right_sum[len(arr) - 1 - i] == left_sum[i]:
            return i
    return -1
