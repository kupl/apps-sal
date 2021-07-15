from collections import defaultdict

def word_problem(rules, from_str, to_str, applications):
    d = defaultdict(list)
    for x, y in rules:
        d[y].append(x)
    b, visited = False, set()
    def dfs(s, p=0):
        nonlocal b
        if s == from_str:
            b = p <= applications
            return
        if p >= len(to_str) or s in visited:
            return
        for i in range(0, len(s)):
            for j in range(i+1, len(s)+1):
                k = s[i:j]
                if k in d:
                    for v in d[k]:
                        dfs(s[:i] + v + s[j:], p + 1)
        visited.add(s)
    dfs(to_str)
    return b
