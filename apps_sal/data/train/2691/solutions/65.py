def solve(s):
    a = ''
    b = 0
    for i in s:
        if i.isdigit():
            a += i
        if not i.isdigit():
            if not a == '':
                b = max(int(a), int(b))
                a = ''
    if not a == '':
        return max(int(a), int(b))
    else:
        return int(b)
