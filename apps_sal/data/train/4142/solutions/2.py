def solve(arr):
    ret = []
    i = len(arr) - 1
    t = None
    while i > -1:
        for j in range(i):
            if arr[j] and set(arr[j]) == set(arr[i]):
                arr[j] = ''
                if not t:
                    t = 0
                t += j
        if t != None:
            ret.append(t + i)
            t = None
        i -= 1
    return sorted(ret)
