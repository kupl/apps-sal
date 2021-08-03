# Prim's algorith for COMPLETE GRAPH: O(N ** 2), O(|V| ** 2)
# Since every node is connected, we can select one node to start with, and calculate all distances to it and take
#   the minimum distance node to it to add to the spanning tree. For the newly added node, update shortest
#   distances to the rest of the nodes (i.e. distance to the current spanning tree). We can then choose the
#   minimum distance node to add to the current spanning tree, and so on.
# Note: it doesn't matter which node in the existing spanning tree that the new node is connected with. We only
#       need its distance to be minimum when connecting to the current spanning tree
#Time: O(N ** 2)
#Sapce: O(M * N)
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        dist = [math.inf] * N

        # mark the starting node
        prev_node = 0
        res = 0

        def getDistance(x, y):
            return abs(points[x][0] - points[y][0]) + abs(points[x][1] - points[y][1])

        for _ in range(N):
            min_dist, min_dist_node = math.inf, -1

            # use distance = None to mark this node has been included in the current spanning tree
            for i in range(N):
                if dist[i] != None:
                    dist[i] = min(dist[i], getDistance(prev_node, i))
                    if dist[i] < min_dist:
                        min_dist, min_dist_node = dist[i], i

            res += min_dist
            prev_node = min_dist_node
            dist[prev_node] = None

        return res
