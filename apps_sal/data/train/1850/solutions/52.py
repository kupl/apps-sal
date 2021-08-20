class Solution:

    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        root = 0
        children = [[] for i in range(N)]
        for (a, b) in edges:
            children[a].append(b)
            children[b].append(a)
        sub_size = [0] * N

        def compute_sub_size(node, parent):
            sub_size[node] = 1
            for child in children[node]:
                if child != parent:
                    compute_sub_size(child, node)
                    sub_size[node] += sub_size[child]
        desc_dist = [0] * N

        def compute_desc_dist(node, parent):
            for child in children[node]:
                if child != parent:
                    compute_desc_dist(child, node)
                    desc_dist[node] += desc_dist[child] + sub_size[child]
        all_dist = [0] * N

        def compute_all_dist(node, parent):
            if parent >= 0:
                all_dist[node] = all_dist[parent] - (desc_dist[node] + sub_size[node])
                all_dist[node] += sub_size[root] - sub_size[node]
            for child in children[node]:
                if child != parent:
                    all_dist[node] += desc_dist[child] + sub_size[child]
            for child in children[node]:
                if child != parent:
                    compute_all_dist(child, node)
        compute_sub_size(0, -1)
        compute_desc_dist(0, -1)
        compute_all_dist(0, -1)
        return all_dist
