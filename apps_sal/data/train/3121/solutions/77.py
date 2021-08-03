def solve(arr):
    for i in arr:
        m = 0
        s = -i
        for j in arr:
            if s == j:
                m = 1
        if m == 0:
            return i
