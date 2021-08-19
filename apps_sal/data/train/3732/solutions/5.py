t = [i * (i - 1) // 2 for i in range(3, 1000)]


def is_madhav_array(arr):
    if len(arr) not in t:
        return False
    sums = {arr[0], arr[1] + arr[2]}
    for (i, j) in zip(t, t[1:]):
        if j > len(arr):
            break
        sums.add(sum(arr[i:j]))
    return len(sums) == 1
