def sort_time(arr):
    s = sorted(arr, key=lambda x: (x[0], arr.index(x)))
    r = [s.pop(0)]
    while s:
        if r[-1][1] > s[-1][0]:
            r.append(s.pop(0))
            continue
        for i in range(len(s)):
            if r[-1][1] <= s[i][0]:
                r.append(s.pop(i))
                break
    return r
