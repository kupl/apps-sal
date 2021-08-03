n = int(input())
a = list(map(int, input().split()))
b = set()
c = set()
for i in a:
    b = set(i | j for j in b)
    b.add(i)
    c.update(b)
print(len(c))
