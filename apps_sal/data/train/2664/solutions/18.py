def solve(s):
    print(s)
    if s == s[::-1] and len(s) % 2 == 0:
        return False
    (left, right) = ([], [])
    l = list(s)
    counter = 0
    while l:
        e = l.pop(0)
        if l:
            e2 = l.pop()
            if e != e2 and counter == 0:
                e2 = e
                counter += 1
            right.insert(0, e2)
        else:
            e = left[-1]
        left.append(e)
    s = ''.join(left + right)
    return s == s[::-1]
