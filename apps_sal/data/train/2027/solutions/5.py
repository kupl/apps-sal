from collections import deque
s = deque(('l' + input())[:-1])
le = []
ri = []
n = 0
while s:
    c = 0
    ref = s[0]
    while s and s[0] == ref:
        c += 1
        s.popleft()
    # print(ref,c)
    if ref == 'l':
        for i in range(c - 1):
            ri.append(n + i + 1)
        le.append(n + c)
        n = n + c
    elif ref == 'r':
        for i in range(c - 1):
            le.append(n + i + 1)
        ri.append(n + c)
        n = n + c
    # print(le,ri)
le.extend(ri[::-1])
print('\n'.join([str(i) for i in le]))
