class DSU:
    def __init__(self, length):
        self.storage = [x for x in range(length)]
        self.rank = [0] * length

    def find(self, val):
        return self.find(self.storage[val]) if val != self.storage[val] else val

    def union(self, val1, val2):
        place_1 = self.find(val1)
        place_2 = self.find(val2)
        if self.rank[place_1] > self.rank[place_2]:
            self.storage[place_2] = self.storage[place_1]
        elif self.rank[place_2] > self.rank[place_1]:
            self.storage[place_1] = self.storage[place_2]
        else:
            self.rank[place_1] += 1
            self.storage[place_2] = self.storage[place_1]


class Solution:
    def distance(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        possible_pairs = []  # (from, to, distance)
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                possible_pairs.append((i, j, self.distance(points[i], points[j])))

        possible_pairs.sort(key=lambda x: x[2])

        result = 0
        index = 0
        count = 0
        dsu = DSU(n)
        while index < len(possible_pairs) and count != n - 1:
            f, to, d = possible_pairs[index]

            x = dsu.find(f)
            y = dsu.find(to)

            if x != y:
                count += 1
                dsu.union(x, y)
                result += d

            index += 1

        return result
