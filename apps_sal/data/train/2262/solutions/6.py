from operator import itemgetter
import collections
r, c, n = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]
e1 = []
e2 = []
e3 = []
e4 = []
for i in range(n):
    if (l[i][0] == 0 or l[i][0] == r or l[i][1] == 0 or l[i][1] == c) and (l[i][2] == 0 or l[i][2] == r or l[i][3] == 0 or l[i][3] == c):
        if l[i][0] == 0 and l[i][1] != c:
            e1.append([i + 1, l[i][0], l[i][1]])
        elif l[i][1] == c and l[i][0] != r:
            e2.append([i + 1, l[i][0], l[i][1]])
        elif l[i][0] == r and l[i][1] != 0:
            e3.append([i + 1, l[i][0], l[i][1]])
        else:
            e4.append([i + 1, l[i][0], l[i][1]])
        if l[i][2] == 0 and l[i][3] != c:
            e1.append([i + 1, l[i][2], l[i][3]])
        elif l[i][3] == c and l[i][2] != r:
            e2.append([i + 1, l[i][2], l[i][3]])
        elif l[i][2] == r and l[i][3] != 0:
            e3.append([i + 1, l[i][2], l[i][3]])
        else:
            e4.append([i + 1, l[i][2], l[i][3]])
e1 = sorted(e1, key=itemgetter(2))
e2 = sorted(e2, key=itemgetter(1))
e3 = sorted(e3, key=itemgetter(2))
e4 = sorted(e4, key=itemgetter(1))
e3.reverse()
e4.reverse()
e = e1 + e2 + e3 + e4

q = []
q = collections.deque(q)
for i in range(len(e)):
    if len(q) == 0:
        q.append(e[i][0])
    else:
        if q[-1] == e[i][0]:
            q.pop()
        else:
            q.append(e[i][0])
if len(q) == 0:
    print('YES')
else:
    print('NO')
