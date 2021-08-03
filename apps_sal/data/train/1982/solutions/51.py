class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        '''
        def dfs(curr, curr_color):
            color[curr] = curr_color
            for next in graph[curr]:
                dfs(next, not curr_color)
        '''

        curr_color = True
        graph = collections.defaultdict(list)
        color = [None] * (N + 1)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        for n in range(1, N + 1):
            if color[n] == None:
                color[n] = curr_color
                queue = collections.deque([n])
                while queue:
                    for _ in range(len(queue)):
                        curr = queue.popleft()
                        for next in graph[curr]:
                            if color[next] == None:
                                color[next] = not curr_color
                                queue.append(next)
                            elif color[next] == curr_color:
                                return False
                    curr_color = not curr_color
        return True
