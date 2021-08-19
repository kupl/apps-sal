input()
A = list(map(int, input().split(' ')))
root = -1
for (i, a) in enumerate(A):
    if i == a - 1:
        root = i
        break
v = [False] * len(A)
if root > -1:
    v[root] = True
changed = 0
for (i, a) in enumerate(A):
    if v[i]:
        continue
    v[i] = True
    l = [i]
    a -= 1
    while not v[a]:
        l.append(a)
        v[a] = True
        a = A[a] - 1
    if a in l:
        if root == -1:
            A[a] = a + 1
            root = a
            changed += 1
        else:
            A[a] = root + 1
            changed += 1
print(changed)
print(' '.join(map(str, A)))
