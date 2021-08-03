class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe_nodes = set()

        for i, node in enumerate(graph):
            if len(node) == 0:
                safe_nodes.add(i)

        while True:
            starting_len = len(safe_nodes)
            for i, node in enumerate(graph):
                all_safe = True
                for j in node:
                    if j not in safe_nodes:
                        all_safe = False
                        break
                if all_safe:
                    safe_nodes.add(i)
            if starting_len == len(safe_nodes):
                break

        return sorted(list(safe_nodes))
