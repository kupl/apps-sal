'''
https://leetcode.com/problems/min-cost-to-connect-all-points/
'''
from typing import List
import heapq


class Solution:
    '''
    Minimum Spanning Tree (Kruskal)
    https://leetcode.com/problems/min-cost-to-connect-all-points/discuss/843940/C%2B%2B-Minimum-Spanning-Tree-(Kruskal)

    Intuition:
    Imagine all the points form a complete graph, and length of an edge is the manhattan distance between the 2 points
    To find the min cost, we therefore need to find the minimum spanning tree

    Algorithm:
    Use the Kruskal algorithm, which invovles min heap to pick the smallest edge, and union-find to check if the edge is redundant.
    Exit when all points are connected.

    The complexity when using sort is O(n * n log (n * n)) - we have n * n edges. Using a min heap is O(k log (n * n)),
    where k is the number of edges we need to pull to complete the tree. It's much smaller than n * n in the average case.
    '''

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def find(ds, i):
            if ds[i] < 0:
                return i
            ds[i] = find(ds, ds[i])
            return ds[i]

        n, ans = len(points), 0
        ds = [-1] * n
        arr = []
        for i in range(n):
            for j in range(i + 1, n):
                heapq.heappush(arr, [abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j])
        while arr:
            dist, i, j = heapq.heappop(arr)
            i, j = find(ds, i), find(ds, j)
            if i != j:
                ans += dist
                ds[i] += ds[j]
                ds[j] = i
                if ds[i] == -n:
                    break
        return ans
