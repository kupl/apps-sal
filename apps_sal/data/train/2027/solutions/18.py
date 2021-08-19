def scape(s):
    first = []
    last = []
    it = 1
    for ch in s:
        if ch == 'l':
            last.append(it)
        else:
            first.append(it)
        it += 1
    for i in range(len(last) - 1, -1, -1):
        first.append(last[i])
    return first


s = input()
ans = []
ans = scape(s)
for i in ans:
    print(i)
