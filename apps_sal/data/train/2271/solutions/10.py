def find(x):
    '''
    xの根を求める
    '''
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]


def union(x, y):
    '''
    xとyの属する集合の併合
    '''
    x = find(x)
    y = find(y)
    
    if x == y:
        return

    if par[x] > par[y]:
        x, y = y, x

    par[x] += par[y]
    par[y] = x


def size(x):
    '''
    xが属する集合の個数
    '''
    return -par[find(x)]


def same(x, y):
    '''
    xとyが同じ集合に属するかの判定
    '''
    return find(x) == find(y)


n, m = map(int, input().split())
p = list(map(int, input().split()))

par = [-1] * n

pos = [-1] * n
for i in range(n):
    pos[p[i]-1] = i

for _ in range(m):
    x, y = map(int, input().split())
    union(x-1, y-1)

res = 0
for i in range(n):
    if same(i, pos[i]):
        res += 1

print(res)
