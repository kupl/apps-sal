def solve(edges, ans):
    n = len(edges)
    visited = set()
    parents = [-1] * (n + 1)
    dp = [0] * (n + 1)
    stack = [1]
    w = float('inf')
    x = -1
    while stack:
        node = stack[-1]
        if node not in visited:
            count = 0
            for kid in edges[node]:
                if parents[kid] == -1:
                    if kid != 1:
                        parents[kid] = node
                elif kid != parents[node]:
                    if kid in visited:
                        count += 1
                    else:
                        stack.append(kid)
            if node == 1:
                count -= 1
            if count == len(edges[node]) - 1:
                stack.pop()
                visited.add(node)
                max_val = 0
                for kid in edges[node]:
                    dp[node] += dp[kid]
                    max_val = max(max_val, dp[kid])
                dp[node] += 1
                max_val = max(max_val, n - dp[node])
                if max_val < w:
                    w = max_val
                    x = node
                elif max_val == w:
                    x = min(x, node)
    ans.append(str(x) + ' ' + str(w))


def main():
    t = int(input())
    ans = []
    for i in range(t):
        n = int(input())
        edges = {}
        for j in range(1, n + 1):
            edges[j] = []
        for j in range(n - 1):
            (x, y) = list(map(int, input().split()))
            edges[x].append(y)
            edges[y].append(x)
        solve(edges, ans)
    print('\n'.join(ans))


main()
