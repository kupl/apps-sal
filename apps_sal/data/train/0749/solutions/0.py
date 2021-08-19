n = int(input())
l = []
for i in range(n):
    l.append([int(x) for x in input().split()])
d = [10**9] * (n)
q = set([int(x) for x in range(1, n)])
d[1] = 0
# print(q)


def extract():
    mini = 10**9
    o = 0
    for i in range(1, len(d)):
        if d[i] < mini and i in q:
            mini = d[i]
            o = i
    q.remove(o)
    return o


while len(q) != 0:
    x = extract()
    for i in range(1, n):
        if i in q and l[x][i] < d[i]:
            d[i] = l[x][i]
print(sum(d[1:]))
