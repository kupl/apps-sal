h = int(input())
a = list(map(int, input().split()))
(w, q) = ([], [])
p = r = 0
for i in a:
    for j in range(i):
        w.append(r)
        q.append(r - (j and p > 1))
    p = i
    r += i
if w == q:
    print('perfect')
else:
    print('ambiguous')
    print(*w)
    print(*q)
