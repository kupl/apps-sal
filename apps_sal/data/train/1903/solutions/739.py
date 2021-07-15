import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def helper(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        edges = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                heapq.heappush(edges, (helper(points[i], points[j]), i, j))
        tree = []
        res = 0
        # print(edges)
        while edges:
            dist, i, j = heapq.heappop(edges)
            flag = False
            for p in range(len(tree)):
                s = tree[p]
                if i in s or j in s:
                    q = j if i in s else i
                    if q not in s:
                        set_num = -1
                        for k in range(len(tree)):
                            st = tree[k]
                            if q in st:
                                set_num = k
                                break
                        if set_num != -1:
                            tree[p] = tree[p].union(tree[k])
                            tree.pop(k)
                        else:
                            s.add(q)
                        res += dist
                    flag = True
                    break
            if not flag:
                tree.append({i, j})
                res += dist
            # print(tree)
        return res
