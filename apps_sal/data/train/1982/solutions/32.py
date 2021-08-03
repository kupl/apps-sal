from collections import defaultdict, deque


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(set)
        for dislike in dislikes:
            graph[dislike[0]].add(dislike[1])
            graph[dislike[1]].add(dislike[0])

        colors = [-1 for i in range(N + 1)]
        queue = deque()
        for i in range(1, N):
            if colors[i] == -1:
                queue.append(i)
                colors[i] = 0
                while len(queue) > 0:
                    cur = queue.popleft()
                    for neighbor in graph[cur]:
                        if colors[neighbor] == -1:
                            colors[neighbor] = 1 - colors[cur]
                            queue.append(neighbor)
                        elif colors[neighbor] == colors[cur]:
                            return False

        return True
