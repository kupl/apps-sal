class Solution:
    parents = [i for i in range(1005)]

    def findParent(i):
        if(Solution.parents[i] != i):
            Solution.parents[i] = Solution.findParent(Solution.parents[i])
        return Solution.parents[i]

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        distances = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                distances.append([distance, i, j])
        distances.sort()
        ans = 0
        for distance in distances:
            if(Solution.findParent(distance[1]) != Solution.findParent(distance[2])):
                Solution.parents[Solution.parents[distance[1]]] = Solution.parents[Solution.parents[distance[2]]]
                ans += distance[0]
        Solution.parents = [i for i in range(1005)]
        return ans
