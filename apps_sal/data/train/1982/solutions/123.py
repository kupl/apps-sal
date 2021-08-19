class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(N + 1)]
        # print(graph)

        for dislike in dislikes:
            # if graph[dislike[0]] == None:
            #     graph[dislike[0]] = []
            # if graph[dislike[1]] == None:
            #     graph[dislike[1]] = []

            graph[dislike[0]].append(dislike[1])
            graph[dislike[1]].append(dislike[0])

        color = {}

        for p in range(N):
            if p in color:
                continue
            color[p] = True

            stack = [p]
            while stack:
                p1 = stack.pop()
                for p2 in graph[p1]:
                    if p2 in color:
                        if color[p2] == color[p1]:
                            return False
                    else:
                        color[p2] = not color[p1]
                        stack.append(p2)

        return True
