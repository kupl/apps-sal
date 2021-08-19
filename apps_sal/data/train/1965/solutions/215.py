class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        def find(comp_id):
            while parents[comp_id] != comp_id:
                parents[comp_id] = parents[parents[comp_id]]
                comp_id = parents[comp_id]
            return comp_id

        def union(id_1, id_2):
            px = find(id_1)
            py = find(id_2)
            parents[py] = px
            return px != py

        # use union find for components
        # init each node as a component
        # once an edge is found (use num 3 first) then
        # union the components, if there is change, then amount of components change
        # if only one component left then the graph is traversable
        parents = [idx for idx in range(n)]
        removed_edges = 0
        for link in edges:
            if link[0] != 3:
                continue
            # only double linked edges first
            if not union(link[1] - 1, link[2] - 1):
                removed_edges += 1

        bob_parents = parents[:]
        for link in edges:
            if link[0] != 1:
                continue
            if not union(link[1] - 1, link[2] - 1):
                removed_edges += 1
        if len(Counter(find(i) for i in parents)) != 1:  # LLRN - use find() instead of referring directly
            return -1

        parents = bob_parents
        for link in edges:
            if link[0] != 2:
                continue
            if not union(link[1] - 1, link[2] - 1):
                removed_edges += 1
        if len(Counter(find(i) for i in parents)) != 1:
            return -1
        return removed_edges
