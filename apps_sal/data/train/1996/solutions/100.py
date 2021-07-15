class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        SAFE, VISITED, UNSAFE = 1, 0, -1
        is_safe = [None] * len(graph)

        def explore(node):
            if not graph[node]:
                is_safe[node] = SAFE
                return

            if is_safe[node] == VISITED:
                is_safe[node] = UNSAFE  # detected cycle
                return

            if is_safe[node] == None:
                is_safe[node] = VISITED
                for child in graph[node]:
                    explore(child)
                    if is_safe[child] == UNSAFE:
                        is_safe[node] = UNSAFE
                        return
                else:
                    is_safe[node] = SAFE
                    return
        
        for node in range(len(graph)):
            if is_safe[node] == None:
                explore(node)
        # print(is_safe)
        return [node for node in range(len(graph)) if is_safe[node] == SAFE]

