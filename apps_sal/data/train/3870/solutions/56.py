def solve(s):
    count = 0
    l = []
    l1 = []
    l1 = list(s)
    l1.reverse()
    for i in s:
        count += 1
        if i == ' ':
            l1.remove(' ')
            l.append(count - 1)
    for j in l:
        l1.insert(j, ' ')
    l1 = ''.join(l1)
    return l1
