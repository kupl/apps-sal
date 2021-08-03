def square_sums_row(n):
    r = []

    def dfs(r):
        if len(r) == n:
            return 1
        for i in range(1, n + 1):
            if not len(r) or (i not in r and not(i + r[-1])**.5 % 1):
                r.append(i)
                if dfs(r):
                    return 1
                r.pop()
        return 0
    return r if dfs(r) else 0
