from typing import List, Dict, Set
from collections import defaultdict


def find_safe_nodes(graph: Dict, rev_graph: Dict):
    outcount_nodes = defaultdict(set)
    for node, list_innodes in list(graph.items()):
        count_outedges = len(list_innodes)
        outcount_nodes[count_outedges].add(node)

    safe_nodes = set()
    while len(outcount_nodes[0]) > 0:
        safe_node = outcount_nodes[0].pop()
        safer_nodes = rev_graph[safe_node]
        for safer_node in safer_nodes:
            prev_outcount = len(graph[safer_node])
            graph[safer_node].remove(safe_node)
            outcount_nodes[prev_outcount].remove(safer_node)
            outcount_nodes[prev_outcount - 1].add(safer_node)
        safe_nodes.add(safe_node)
    return safe_nodes


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        list_graph = graph
        graph = defaultdict(set)
        rev_graph = defaultdict(set)

        for node1, list_node2 in enumerate(list_graph):
            for node2 in list_node2:
                graph[node1].add(node2)
                rev_graph[node2].add(node1)

        for i in range(len(list_graph)):
            if i not in graph:
                graph[i] = set()
            if i not in rev_graph:
                rev_graph[i] = set()

        safe_nodes = find_safe_nodes(graph, rev_graph)
        return sorted(safe_nodes)


s = Solution()

print((s.eventualSafeNodes(graph=[[1, 2], [2, 3], [5], [0], [5], [], []])))
print((s.eventualSafeNodes(graph=[[1, 2], [2, 3], [5], [0], [5], [], []]) == [2, 4, 5, 6]))

print((s.eventualSafeNodes([[], [0, 2, 3, 4], [3], [4], []])))
print((s.eventualSafeNodes([[], [0, 2, 3, 4], [3], [4], []]) == [0, 1, 2, 3, 4]))
