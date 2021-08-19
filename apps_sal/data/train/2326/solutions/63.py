def main(n, a):
    ret = [0] * n
    d = {}
    for (i, x) in enumerate(a):
        if x in d:
            d[x].append(i)
        else:
            d[x] = [i]
    v = sorted(list(d.keys()), reverse=True)
    cnt_idx = 0
    min_idx = n + 1
    for (i, x) in enumerate(v):
        cnt_idx += len(d[x])
        min_idx = min(min_idx, d[x][0])
        nx = 0
        if i < len(v) - 1:
            nx = v[i + 1]
        ret[min_idx] += cnt_idx * (x - nx)
    return ret


n = int(input())
a = list(map(int, input().split()))
print(*main(n, a), sep='\n')
