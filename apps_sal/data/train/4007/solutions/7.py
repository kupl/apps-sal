def finding_k(arr):
    # your code here
    maxValue = max(arr) - min(arr)
    k = 0
    while maxValue > 0:
        if len(set(map(lambda x: x % maxValue, arr))) == 1:
            k = maxValue
            break
        maxValue -= 1
    if k:
        return k
    else:
        return -1
