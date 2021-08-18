class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        def make_graph(dislikes):
            graph = defaultdict(list)
            for dl in dislikes:
                graph[dl[1]].append(dl[0])
                graph[dl[0]].append(dl[1])
            return graph

        graph = make_graph(dislikes)
        visited = {}

        for i in range(1, N + 1):
            if i in visited:
                continue
            visited[i] = 'red'
            stack = [[i, visited[i]]]

            while stack:
                num, pos = stack.pop(0)
                for next_num in graph[num]:
                    if next_num in visited:
                        if visited[next_num] == pos:

                            return False
                    else:
                        if pos == 'blue':
                            next_pos = 'red'
                        else:
                            next_pos = 'blue'
                        visited[next_num] = next_pos
                        stack.append([next_num, next_pos])
        return True
