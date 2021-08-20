def solve(arr):
    arr.sort()
    l = len(arr)
    neg = []
    pos = []
    for i in arr:
        if i < 0:
            neg.append(i)
        else:
            pos.append(i)
    if len(neg) > len(pos):
        for i in neg:
            if abs(i) not in pos:
                return i
    else:
        for i in pos:
            if -i not in neg:
                return i
