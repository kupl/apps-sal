from sys import stdin
(name1, name2) = [x.strip() for x in input().split()]
n = int(input())
print(name1, name2)
d = {name1, name2}
for i in range(n):
    (n1, n2) = [x.strip() for x in input().split()]
    d.discard(n1)
    d.add(n2)
    ans = ' '.join(d)
    print(ans)
