# DFS / Topological Method
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        WHITE, GREY, BLACK = 0, 1, 2
        result = []

        # 1) assign colors for all nodes
        color = defaultdict()
        for i in range(len(graph)):
            color[i] = WHITE

        # 2) dfs the nodes
        def dfs(node):
            if color[node] != WHITE:          # this node was visited, could be grey or black
                return color[node] == BLACK       # shortcut return

            color[node] = GREY                    # visiting node so color it grey
            for neigh in graph[node]:           # visit all neighbors of current node
                if not dfs(neigh):
                    return False

            color[node] = BLACK                   # Done visiting this node so mark it Black
            return True

        # 3) check all nodes in graph
        for i in range(len(graph)):             # check each node in graph
            if not graph[i]:             # if node has no outgoing edges it must be a terminal node
                result.append(i)
            elif dfs(i):
                result.append(i)

        return result

    # Complexity: O(N+E)   N-nodes, for each node, have to explore all its edges.
