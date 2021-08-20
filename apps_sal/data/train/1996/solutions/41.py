class Solution:

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        out_degrees = [0] * n
        node_lsts = collections.defaultdict(list)
        queue = []
        for i in range(len(graph)):
            out_degrees[i] = len(graph[i])
            if out_degrees[i] == 0:
                queue.append(i)
            for j in graph[i]:
                node_lsts[j].append(i)
        for term_node in queue:
            for n in node_lsts[term_node]:
                out_degrees[n] -= 1
                if out_degrees[n] == 0:
                    queue.append(n)
        return sorted(queue)
