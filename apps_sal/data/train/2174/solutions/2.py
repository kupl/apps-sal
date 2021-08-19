(n, a, b) = (input(), set(), set())
for i in map(int, input().split()):
    b = set((i | j for j in b))
    b.add(i)
    a.update(b)
print(len(a))
