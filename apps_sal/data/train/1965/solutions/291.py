class DisjointSet:
    def __init__(self, number_of_sites):
        self.parent = [i for i in range(number_of_sites + 1)]
        self.children_site_count = [1 for _ in range(number_of_sites + 1)]
        self.component_count = number_of_sites

    def find_root(self, site):
        root = site
        while root != self.parent[root]:
            root = self.parent[root]
        while site != root:
            site, self.parent[site] = self.parent[site], root
        return root

    def is_connected(self, site_1, site_2):
        return self.find_root(site_1) == self.find_root(site_2)

    def union(self, site_1, site_2):
        site_1_root = self.find_root(site_1)
        site_2_root = self.find_root(site_2)
        if site_1_root == site_2_root:
            return False

        if self.children_site_count[site_1_root] < self.children_site_count[site_2_root]:
            self.parent[site_1_root] = site_2_root
            self.children_site_count[site_2_root] += self.children_site_count[
                site_1_root]
        else:
            self.parent[site_2_root] = site_1_root
            self.children_site_count[site_1_root] += self.children_site_count[
                site_2_root]
        self.component_count -= 1
        return True


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice_disjoint_set = DisjointSet(n)
        bob_disjoint_set = DisjointSet(n)

        TYPE_OF_COMMON_EDGES = 3
        TYPE_OF_ALICE_EDGES = 1
        TYPE_OF_BOB_EDGES = 2

        common_edges = filter(lambda edge: edge[0] == TYPE_OF_COMMON_EDGES, edges)
        alice_edges = filter(lambda edge: edge[0] == TYPE_OF_ALICE_EDGES, edges)
        bob_edges = filter(lambda edge: edge[0] == TYPE_OF_BOB_EDGES, edges)

        redundant = 0
        for _, u, v in common_edges:
            unioned_in_alice = alice_disjoint_set.union(u, v)
            unioned_in_bob = bob_disjoint_set.union(u, v)
            if (not unioned_in_alice) and (not unioned_in_bob):
                redundant += 1

        for _, u, v in bob_edges:
            if not bob_disjoint_set.union(u, v):
                redundant += 1

        for _, u, v in alice_edges:
            if not alice_disjoint_set.union(u, v):
                redundant += 1

        return redundant if alice_disjoint_set.component_count == 1 and bob_disjoint_set.component_count == 1 else -1
