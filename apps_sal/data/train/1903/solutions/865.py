class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        Big idea: Union find to detect cycles. Create all edges, sort by distance. Look at each edge and add it if it doesn't make a cycle. Return the total of the added edges.
        """
        edges = []
        for i in range(len(points)):
            p1 = tuple(points[i])
            for j in range(i + 1, len(points)):
                p2 = tuple(points[j])
                dist = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
                edges.append((dist, p1, p2))
        edges.sort()
        self.roots = {(x, y): (x, y) for (x, y) in points}
        self.ranks = {(x, y): 0 for (x, y) in points}
        ans = 0
        for edge in edges:
            (dist, p1, p2) = edge
            if self.union(p1, p2):
                ans += dist
        return ans

    def union(self, p1, p2):
        (p1_root, p2_root) = (self.find(p1), self.find(p2))
        if p1_root == p2_root:
            return False
        if self.ranks[p1_root] < self.ranks[p2_root]:
            self.roots[p1_root] = p2_root
        elif self.ranks[p1_root] > self.ranks[p2_root]:
            self.roots[p2_root] = p1_root
        else:
            self.roots[p1_root] = p2_root
            self.ranks[p2_root] += 1
        return True

    def find(self, p):
        if p != self.roots[p]:
            self.roots[p] = self.find(self.roots[p])
        return self.roots[p]
