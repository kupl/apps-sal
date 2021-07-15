def solve(arr):
    pos = []
    neg = []
    for i in arr:
        if i < 0:
            neg.append(i)
        else:
            pos.append(i)
    for i in neg:
        if abs(i) not in pos:
            return i
            break
    for j in pos:
        if -j not in neg:
            return j
            break
