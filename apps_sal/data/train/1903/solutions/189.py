class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def main(arr):
            if len(arr) < 1:
                return 0
            node = 0
            answer = 0
            n = len(arr)
            visit = set()
            global_dist = [float('inf')] * n
            while n > 1:
                cur_x, cur_y = arr[node]
                visit.add(node)

                for j in range(len(arr)):
                    if j in visit:
                        continue
                    x, y = arr[j]
                    global_dist[j] = min(global_dist[j], abs(x - cur_x) + abs(y - cur_y))

                next_node = -1
                next_dist = float('inf')
                for idx, dist in enumerate(global_dist):
                    if dist < next_dist:
                        next_dist = dist
                        next_node = idx
                node = next_node
                answer += next_dist

                global_dist[next_node] = float('inf')

                n -= 1

            return answer
        return main(points)
