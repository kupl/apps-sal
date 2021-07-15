n, p, q = input(), set(), set()
for i in map(int, input().split()):
    q = set(i | j for j in q)
    q.add(i)
    p.update(q)
print(len(p))
