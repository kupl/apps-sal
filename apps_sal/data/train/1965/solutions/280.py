
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        mm = [collections.defaultdict(set), collections.defaultdict(set), collections.defaultdict(set)]
        for t, u, v in edges:
            mm[t - 1][u].add(v)
            mm[t - 1][v].add(u)

        n_edges = 0

        super_nodes = {}
        super_nodes_list = []
        n_super_nodes = 0

        def dfs(type):
            visited = set()
            nonlocal n_edges

            def search(node):
                if node in visited:
                    return
                visited.add(node)
                neis = mm[type][node].union(mm[2][node])
                for node2 in neis:
                    if node2 not in visited:
                        search(node2)

            search(1)
            if len(visited) != n:
                n_edges += float('inf')

        def create_super_nodes():
            total_visited = set()
            cur_visited = set()
            nonlocal n_super_nodes

            def search(node):
                nonlocal n_edges

                if node in cur_visited:
                    return
                cur_visited.add(node)
                for node2 in mm[2][node]:
                    if node2 not in cur_visited:
                        n_edges += 1
                        search(node2)

            for node in range(1, n + 1):
                cur_visited = set()
                if node not in total_visited:
                    search(node)
                    # super_nodes_list.append(cur_visited)
                    total_visited.update(cur_visited)
                    n_super_nodes += 1
                    # for node2 in cur_visited:
                    #     super_nodes[node2] = cur_visited

        create_super_nodes()
        dfs(0)
        dfs(1)
        n_edges += (n_super_nodes - 1) * 2
        sol = len(edges) - (n_edges)
        if sol == float('-inf'):
            return -1
        return sol
