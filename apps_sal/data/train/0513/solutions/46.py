import sys
readline = sys.stdin.readline

sys.setrecursionlimit(10**6)


def main():
    N = int(input())
    As = list(map(int, input().split()))

    query = (list(map(int, readline().strip().split())) for _ in range(N-1))

    tree = [[] for _ in range(N)]
    for u, v in query:
        tree[u-1].append(v-1)
        tree[v-1].append(u-1)

    inf = 10 ** 18
    dp = [inf] * (N+1)
    ans = [0] * N

    def dfs(node, parent):
        v = As[node]
        lb = binary_search(dp, v)
        old = dp[lb]
        dp[lb] = v
        ans[node] = binary_search(dp, inf)
        for child in tree[node]:
            if child == parent:
                continue
            dfs(child, node)
        dp[lb] = old

    dfs(0, 0)

    for k in range(N):
        print((ans[k]))


def binary_search(seq, v):
    left = 0
    right = len(seq) - 1
    center = right // 2

    while left != right:
        if v <= seq[center]:
            right = center
        else:
            left = center+1
        center = (right + left) // 2

    return center


def __starting_point():
    main()

__starting_point()
