import sys
input = sys.stdin.readline

N = int(input())
D = [None] + [int(input()) for _ in range(N)]

parent = [None] * (N+1)
size = [None] + [1] * N # 部分木の頂点数、自分を含む
d_to_i = {d:i for i,d in enumerate(D)}
D_desc = sorted(D[1:],reverse=True)
D_subtree = [0] * (N+1)
edges = []

bl = True
for d in D_desc[:-1]:
    i = d_to_i[d]
    d_parent = d - N + 2*size[i]
    if d_parent not in d_to_i:
        bl = False
        break
    p = d_to_i[d_parent]
    edges.append('{} {}'.format(i,p))
    parent[i] = p
    size[p] += size[i]
    D_subtree[p] += D_subtree[i] + size[i]

root = d_to_i[D_desc[-1]]
bl &= (D_subtree[root] == D[root])

if bl:
    print('\n'.join(edges))
else:
    print(-1)
