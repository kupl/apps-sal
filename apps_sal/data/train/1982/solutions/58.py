from collections import deque


class Solution:

    def expandColorBFS(self, start, graph, colors):
        if colors[start] != 0:
            return True
        q = deque()
        q.append(start)
        colors[start] = -1
        while q:
            cur = q.popleft()
            for neighbour in graph[cur]:
                if colors[neighbour] == 0:
                    q.append(neighbour)
                    colors[neighbour] = -colors[cur]
                elif colors[cur] == colors[neighbour]:
                    return False
        return True

    def expandColorDFS(self, cur, graph, colors, cur_color):
        if colors[cur] != -1:
            return cur_color == colors[cur]
        colors[cur] = cur_color
        neighbour_color = 0 if colors[cur] == 1 else 1
        for neighbour in graph[cur]:
            if not self.expandColorDFS(neighbour, graph, colors, neighbour_color):
                return False
        return True

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        colors = [0 for _ in range(N + 1)]
        graph = defaultdict(set)
        for dislike in dislikes:
            graph[dislike[0]].add(dislike[1])
            graph[dislike[1]].add(dislike[0])
        for idx in range(1, N + 1):
            if not self.expandColorBFS(idx, graph, colors):
                return False
        return True
