n = eval(input())
r = list(map(int, input().split()))
tree = dict()
i = 1
for j in r:
    c = tree.get(j)
    if c:
        tree[j].append(i)
    else:
        tree[j] = [i]
    if not tree.get(i):
        tree[i] = []
    i += 1
s = []
for elem in tree:
    if not tree[elem]:
        s.append(str(elem))
print(' '.join(s))
