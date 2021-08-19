def left(h, m, n):
    k = 0
    L = [False] * n
    for i in range(n):
        if h[i] >= k + 1:
            k += 1
            if k == m:
                L[i] = True
                k -= 1
        else:
            k = h[i]
    return L


def right(h, m, n):
    k = 0
    R = [False] * n
    for i in range(n - 1, -1, -1):
        if h[i] >= k + 1:
            k += 1
            if k == m:
                R[i] = True
                k -= 1
        else:
            k = h[i]
    return R


def comp(h, m, n):
    l = left(h, m, n)
    r = right(h, m, n)
    for i in range(n):
        if l[i] == True and r[i] == True:
            return True
    return False


for _ in range(int(input().strip())):
    blocks = int(input().strip())
    blocks_height = list(map(int, input().strip().split()))
    su = sum(blocks_height)
    start = 1
    end = blocks + 1
    while start < end - 1:
        mid = (start + end) // 2
        if comp(blocks_height, mid, blocks):
            start = mid
        else:
            end = mid
    print(su - start * start)
