def solve(s):
    li = []
    for k in s.splitlines():
        c = [0]
        for (i, j) in reversed(list(zip(k.split(' ')[0], k.split(' ')[1]))):
            if int(i) + int(j) + int(c[-1]) > 9:
                c.append(str(int(i) + int(j) + int(c[-1]))[0])
            else:
                c.append(0)
        li.append('No carry operation' if c.count('1') < 1 else f"{c.count('1')} carry operations")
    return '\n'.join(li)
