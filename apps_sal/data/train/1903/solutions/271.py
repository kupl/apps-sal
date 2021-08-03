class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        self.rank = [1 for _ in range(n)]
        self.parent = [i for i in range(n)]
        distance = []
        for i in range(n - 1):
            for j in range(i + 1, n):
                dis = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                distance.append((dis, i, j))
        distance.sort(key=lambda x: x[0])
        ans = 0
        count = 0
        for dis, u, v in distance:
            if self.find(u) == self.find(v):
                continue
            ans += dis
            self.union(u, v)
            count += 1
            if count == n - 1:
                break
        return ans

    def union(self, a, b):
        parenta = self.find(a)
        parentb = self.find(b)
        if parenta == parentb:
            return
        if self.rank[parenta] > self.rank[parentb]:
            self.parent[parentb] = parenta
            self.rank[parenta] += self.rank[parentb]
        else:
            self.parent[parenta] = parentb
            self.rank[parentb] += self.rank[parenta]
        return

    def find(self, a):
        if self.parent[a] == a:
            return a
        else:
            self.parent[a] = self.find(self.parent[a])
            return self.parent[a]
