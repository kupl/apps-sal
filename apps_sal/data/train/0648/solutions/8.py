def query(i, j):
    cnt = 0
    past = arr[i]
    limit = 0
    ind = i
    for idx in range(i + 1, n):
        curr = arr[idx]
        if curr != past and curr > past:
            cnt += 1
            past = curr
            ind = idx
            limit = 0
        if cnt == j:
            return ind + 1
        if curr <= past:
            limit += 1
        if limit > 100:
            break
    return ind + 1


def update(l, r, v):
    for idx in range(l, r + 1):
        arr[idx] += v


(n, q) = list(map(int, input().split()))
arr = list(map(int, input().split()))
for _ in range(q):
    a = list(map(int, input().split()))
    if a[0] - 1:
        update(a[1] - 1, a[2] - 1, a[3])
    else:
        print(query(a[1] - 1, a[2]))
