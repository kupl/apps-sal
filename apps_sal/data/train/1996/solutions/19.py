class Solution:

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited = set()
        states = [None] * len(graph)

        def verify(i):
            if states[i] is not None:
                return states[i]
            if i in visited:
                return False
            visited.add(i)
            for j in graph[i]:
                stable = verify(j)
                if j in visited:
                    visited.remove(j)
                states[j] = stable
                if not stable:
                    return False
            return True
        verified_unstable = set()
        for i in range(len(graph)):
            if states[i] is not None:
                continue
            states[i] = verify(i)
        return [i for (i, val) in enumerate(states) if val == True]
