class Solution:

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        colors = [0] * (N + 1)
        from collections import defaultdict
        g = defaultdict(set)
        for dislike in dislikes:
            g[dislike[0]].add(dislike[1])
            g[dislike[1]].add(dislike[0])
        from collections import deque
        q = deque()
        for i in range(1, N + 1):
            if i not in g:
                colors[i] = 1
            if colors[i]:
                continue
            colors[i] = 1
            q.append(i)
            while q:
                cur = q.popleft()
                for neighbor in g[cur]:
                    if colors[neighbor]:
                        if colors[neighbor] == colors[cur]:
                            return False
                        continue
                    colors[neighbor] = 1 if colors[cur] == -1 else -1
                    q.append(neighbor)
        return True
