class Solution:
    def manhattan_distance(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def find(self, x):
        while x in self.parent:
            while self.parent[x] in self.parent:
                self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        x_find = self.find(x)
        y_find = self.find(y)
        if(x_find != y_find):
            self.parent[x_find] = y_find
            return True

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        self.parent = {}

        ls = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                ls.append([self.manhattan_distance(points[i], points[j]), i, j])
        # print(ls)
        ls = sorted(ls, key=lambda x: x[0])
        # print(ls)

        ans = 0
        for i in range(len(ls)):
            if(self.union(ls[i][1], ls[i][2])):
                ans += ls[i][0]
            # print(self.parent)
        return ans
