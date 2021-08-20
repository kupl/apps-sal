def solve(arr):
    stack = []
    for i in arr:
        x = arr[:]
        x.remove(i)
        stack.append(([i], x))
    while True:
        (a, b) = stack.pop(0)
        v = a[-1]
        (a1, a2) = (a[:], a[:])
        (b1, b2) = (b[:], b[:])
        if v * 2 in b:
            a1.append(v * 2)
            b1.remove(v * 2)
            stack.append((a1, b1))
        if not v % 3:
            if v // 3 in b:
                a2.append(v // 3)
                b2.remove(v // 3)
                stack.append((a2, b2))
        if not b1:
            return a1
        if not b2:
            return a2
