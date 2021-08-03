from collections import deque


class Solution:

    def expandColorBFS(self, start, graph, colors):
        if colors[start] != -1:
            return True
        q = deque()
        q.append(start)
        colors[start] = 0
        while q:
            cur = q.popleft()
            for neighbour in graph[cur]:
                if colors[neighbour] == -1:
                    q.append(neighbour)
                    colors[neighbour] = 0 if colors[cur] == 1 else 1
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
        # -1 unvisited, 0 and 1 are the 2 groups
        colors = [-1 for _ in range(N + 1)]
        graph = defaultdict(set)
        for dislike in dislikes:
            graph[dislike[0]].add(dislike[1])
            graph[dislike[1]].add(dislike[0])

        for idx in range(1, N + 1):
            if colors[idx] == -1:
                if not self.expandColorDFS(idx, graph, colors, 0):
                    return False

        return True

        # for each dislike a,b
        # if we want a's group to differ from b's group
