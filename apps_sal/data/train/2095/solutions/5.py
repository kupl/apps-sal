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
ret = 0
for i, a in enumerate(arr):
    if v[i]:
        continue
    v[i] = True
    curl = [i]
    a -= 1
    while not v[a]:
        curl.append(a)
        v[a] = True
        a = arr[a] - 1
    if a in curl:
        if root == -1:
            arr[a] = a + 1
            root = a
            ret += 1
        else:
            arr[a] = root + 1
            ret += 1
print(ret)
print(' '.join(map(str, arr)))
