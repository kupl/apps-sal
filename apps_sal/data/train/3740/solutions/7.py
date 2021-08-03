def sort_time(arr):
    if len(arr) == 0:
        return []
    r_max = '23:59'
    r_min = '00:00'
    rr = arr[:]
    ret = []
    k = 0
    for i in range(len(arr)):
        for j in range(len(rr)):
            if r_min <= rr[j][0] < r_max:
                r_max = rr[j][0]
                k = j
                if r_max == r_min:
                    break
        ret.append(rr[k])
        r_min = rr[k][1]
        r_max = '23:59'
        rr.pop(k)
        k == 0
        if rr and max(rr)[0] < r_min:
            r_min = min(rr)[0]
    return ret
