s = list(input())
t = list(input())
arr = list((x - 1 for x in map(int, input().split())))
(n, m) = (len(arr), len(t))


def binary_search():
    (f, e) = (0, n)
    while f <= e:
        mid = f + e >> 1
        vis = [0] * n
        for i in range(mid):
            vis[arr[i]] = 1
        (idx, found) = (0, 0)
        for i in range(n):
            if not vis[i] and s[i] == t[idx]:
                idx += 1
            if idx == m:
                found = 1
                break
        if found:
            f = mid + 1
        else:
            e = mid - 1
    return f - 1


print(binary_search())
