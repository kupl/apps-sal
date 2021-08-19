def dfs(index, s, edges, visited):
    indices = []
    vals = []
    stack = [index]
    while stack:
        index = stack.pop()
        if index not in visited:
            visited.add(index)
            indices.append(index)
            vals.append(s[index])
            for kid in edges[index]:
                stack.append(kid)
    indices.sort()
    vals.sort()
    for index in indices:
        s[index] = vals.pop(0)


class Solution:

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        visited = set()
        s = list(s)
        edges = {}
        for (a, b) in pairs:
            if a not in edges.keys():
                edges[a] = []
            if b not in edges.keys():
                edges[b] = []
            edges[a].append(b)
            edges[b].append(a)
        for i in edges.keys():
            if i not in visited:
                dfs(i, s, edges, visited)
        return ''.join(s)
