(N, M, C) = list(map(int, input().split()))
tree = [0] * (N + 1)


def add(u, k):
    while u < len(tree):
        tree[u] += k
        u += u & -u


def query(k):
    ans = 0
    while k:
        ans += tree[k]
        k -= k & -k
    return ans


def solve():
    for _ in range(M):
        op = input().split()
        if op[0] == 'Q':
            print(query(int(op[1])) + C)
        else:
            (u, v, k) = (int(op[1]), int(op[2]), int(op[3]))
            add(u, k)
            add(v + 1, -k)


def __starting_point():
    solve()


__starting_point()
