class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        s = set(initial)
        go_visit = set()
        del_node, length = min(initial), 0

        def helper(node, visit):
            for i in range(len(graph[node])):
                if graph[node][i] == 1 and i not in visit:
                    visit.add(i)
                    helper(i, visit)
        for node in range(len(graph)):
            if node not in go_visit:
                visit = set()
                visit.add(node)
                helper(node, visit)
                temp = visit & s
                if len(temp) == 1:
                    if length < len(visit) or (length == len(visit) and list(temp)[0] < del_node):
                        del_node = list(temp)[0]
                        length = len(visit)
                go_visit |= visit
        return del_node
