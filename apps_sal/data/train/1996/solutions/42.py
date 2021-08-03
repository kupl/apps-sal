class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        state = ['UNPROCESSED'] * n

        def isAcyclic(node):
            if state[node] == 'PROCESSING':
                return False
            elif state[node] == 'PROCESSED':
                return True
            else:
                state[node] = 'PROCESSING'
                if any(not isAcyclic(nei) for nei in graph[node]):
                    return False
                state[node] = 'PROCESSED'
                return True
        return list(filter(isAcyclic, list(range(n))))
