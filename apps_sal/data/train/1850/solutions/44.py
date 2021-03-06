class Solution:

    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        if N == 1:
            return [0]
        neighbors = {}
        for edge in edges:
            a = edge[0]
            b = edge[1]
            if a not in neighbors:
                neighbors[a] = []
            if b not in neighbors:
                neighbors[b] = []
            neighbors[a].append(b)
            neighbors[b].append(a)
        num_descendents = {}
        children = {}
        parent = {}

        def build_children(n, p):
            parent[n] = p
            children[n] = []
            for neighbor in neighbors[n]:
                if neighbor == p:
                    continue
                children[n].append(neighbor)
                build_children(neighbor, n)
            return
        build_children(0, None)

        def build_descendents(n):
            num_descendents[n] = 0
            for child in children[n]:
                num_descendents[n] += 1 + build_descendents(child)
            return num_descendents[n]
        build_descendents(0)
        root_dist = {0: 0}
        queue = children[0].copy()
        while queue != []:
            curr = queue.pop()
            p = parent[curr]
            root_dist[curr] = root_dist[p] + 1
            for child in children[curr]:
                queue.append(child)
        root_sum_dist = 0
        for n in range(N):
            root_sum_dist += root_dist[n]
        queue = children[0].copy()
        sum_dist = {0: root_sum_dist}
        while queue != []:
            curr = queue.pop()
            p = parent[curr]
            desc_curr = num_descendents[curr]
            other_kids_and_desc = num_descendents[p] - 1 - desc_curr
            above_parent = num_descendents[0] - num_descendents[p]
            sum_dist[curr] = sum_dist[p] - desc_curr + other_kids_and_desc + above_parent
            for child in children[curr]:
                queue.append(child)
        ans = []
        for n in range(N):
            ans.append(sum_dist[n])
        return ans
