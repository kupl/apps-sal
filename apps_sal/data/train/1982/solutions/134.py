class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        def bfs(i):
            stack = []
            color[i] = 0
            stack.append(i)
            while stack:
                cur = stack.pop()
                for nei in dislike_adj[cur]:
                    if color[nei] == color[cur]:
                        return False
                    if color[nei] == -1 and color[nei] != color[cur]:
                        stack.append(nei)
                        color[nei] = 1 - color[cur]
            return True
        
        dislike_adj = collections.defaultdict(list)
        color = {}
        for d in dislikes:
            first = d[0]
            second = d[1]
            dislike_adj[first].append(second)
            dislike_adj[second].append(first)
        for i in range(1, N+1):
            color[i] = color.get(i, -1)
        for i in range(1, N+1):
            if color[i] == -1:
                if not bfs(i):
                    return False
        return True
