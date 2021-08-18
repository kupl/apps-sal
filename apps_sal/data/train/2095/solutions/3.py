n = int(input())
arr = list(map(int, input().split(' ')))
root = -1
for i, a in enumerate(arr):
    if i == a - 1:
        root = i
        break
v = [False] * len(arr)
if root > -1:
    v[root] = True
ans = 0
for i, a in enumerate(arr):
    if v[i]:
        continue
    v[i] = True
    l = [i]
    a -= 1
    while not v[a]:
        l.append(a)
        v[a] = True
        a = arr[a] - 1
    if a in l:
        if root == -1:
            arr[a] = a + 1
            root = a
            ans += 1
        else:
            arr[a] = root + 1
            ans += 1
print(ans)
print(' '.join(map(str, arr)))
