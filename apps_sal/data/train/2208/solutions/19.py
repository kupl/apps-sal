import sys


def main():
    def input():
        return sys.stdin.readline()[:-1]

    N, k = list(map(int, input().split()))

    parent = [k for k in range(N)]

    def find(x):
        if parent[x] == x:
            return x
        else:
            parent[x] = find(parent[x])
            return find(parent[x])

    def unite(x, y):
        parent[find(x)] = find(y)
    ans = 0
    for q in range(k):
        x, y = list(map(int, input().split()))
        if find(x - 1) == find(y - 1):
            ans += 1
        else:
            unite(x - 1, y - 1)
    print(ans)


def __starting_point():
    main()


__starting_point()
