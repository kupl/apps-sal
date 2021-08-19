(n1, n2) = input().split()
n = int(input())
names = [input().split() for i in range(n)]
sel = set([n1, n2])
for (killed, next) in names:
    print(' '.join(sel))
    sel.remove(killed)
    sel.add(next)
print(' '.join(sel))
