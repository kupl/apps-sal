def solve(arr):
    sum = 0
    times = 0
    ele = {}
    for i in arr:
        if i in ele:
            ele[i] = ele[i] + i
        else:
            ele[i] = i
        sum = sum + i
    for (k, v) in ele.items():
        if v == sum:
            if -k not in arr:
                times = sum / k
    if times > 1:
        sum = sum / times
    return sum
