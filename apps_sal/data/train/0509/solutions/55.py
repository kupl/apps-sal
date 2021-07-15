# https://atcoder.jp/contests/arc108/submissions/18282738

def main():
    from collections import deque
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split())

    g = tuple(list() for _ in range(n))
    for _ in range(m):
        u, v, c = (int(x) - 1 for x in input().split())
        g[u].append((v, c))
        g[v].append((u, c))

    def make_label(r):
        ret = [-1] * n
        ret[r] = 0

        vis = [False] * n
        vis[r] = True

        dq = deque()
        dq.append(r)

        while dq:
            v = dq.popleft()
            for u, c in g[v]:
                if vis[u]:
                    continue
                vis[u] = True
                if ret[v] == c:
                    if c == n:
                        ret[u] = 0
                    else:
                        ret[u] = c + 1
                else:
                    ret[u] = c
                dq.append(u)
        return ret

    label = make_label(0)
    ans = map(lambda e: e + 1, label)
    print(*ans, sep='\n')


def __starting_point():
    main()

__starting_point()
