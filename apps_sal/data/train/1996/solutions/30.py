from typing import Dict, List, Set


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        result = []
        graph_map: Dict[int, Set[int]] = {}
        reverse_graph_map: Dict[int, Set[int]] = {}
        for i, edges in enumerate(graph):
            graph_map[i] = set(edges)
            for n in edges:
                reverse_graph_map.setdefault(n, set())
                reverse_graph_map[n].add(i)

        while True:
            to_remove = set()
            for i, edges in list(graph_map.items()):
                if len(edges) == 0:
                    to_remove.add(i)
            if len(to_remove) == 0:
                break

            result.extend(to_remove)

            for i in to_remove:
                del graph_map[i]
                for n in reverse_graph_map.get(i, set()):
                    graph_map[n].remove(i)

        return sorted(result)
