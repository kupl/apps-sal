N = int(input())
A = [int(_) for _ in input().split()]


def compress_coord(raw):
    v_i = {}
    for i, v in enumerate(raw):
        if v not in v_i:
            v_i[v] = []
        v_i[v] += [i]
    return v_i


a_i = compress_coord(A)
A2 = sorted(a_i.keys())[::-1]
ans = [0] * N
n = 0
i = 10**10
for iv, a in enumerate(A2):
    if iv < len(A2) - 1:
        anext = A2[iv + 1]
    else:
        anext = 0
    i = min(i, a_i[a][0])
    n += len(a_i[a])
    ans[i] += n * (a - anext)
print(*ans, sep='\n')
