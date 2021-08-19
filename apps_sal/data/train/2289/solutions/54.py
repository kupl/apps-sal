def n2a(x):
    return chr(x + ord('a'))


def a2n(x):
    return ord(x) - ord('a')


def main(a):
    nc = 26
    n = len(a)
    ary = []
    tmp = [0] * nc
    mi = set(range(nc))
    for i in range(n - 1, -1, -1):
        x = a2n(a[i])
        mi.discard(x)
        tmp[x] += 1
        if len(mi) == 0:
            ary.append(tmp.copy())
            tmp = [0] * nc
            mi = set(range(nc))
    if any(tmp):
        ary.append(tmp)
    ans = []
    now = 0
    tmp = ary.pop()
    if all(tmp):
        ans.append('a')
        while a[now] != 'a':
            tmp[a2n(a[now])] -= 1
            now += 1
        tmp[a2n(a[now])] -= 1
        now += 1
    else:
        for i in range(nc):
            if tmp[i] == 0:
                ans.append(n2a(i))
                break
        if not ary:
            return ans
        ntmp = ary.pop()
        for j in range(nc):
            tmp[j] += ntmp[j]
        while a2n(a[now]) != i:
            tmp[a2n(a[now])] -= 1
            now += 1
        tmp[a2n(a[now])] -= 1
        now += 1
    while True:
        for i in range(nc):
            if tmp[i] == 0:
                ans.append(n2a(i))
                break
        if not ary:
            return ans
        ntmp = ary.pop()
        for j in range(nc):
            tmp[j] += ntmp[j]
        while a2n(a[now]) != i:
            tmp[a2n(a[now])] -= 1
            now += 1
        tmp[a2n(a[now])] -= 1
        now += 1


a = input()
print(*main(a), sep='')
'\nbcdefghijklmnopqrstuvwxyza\n\naabbccaabca\naab / bccaa / bca\n\n'
