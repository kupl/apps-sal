input()
a, b = set(), set()
for i in map(int, input().split()):
  a = {i | j for j in a}
  a.add(i)
  b.update(a)
print(len(b))
