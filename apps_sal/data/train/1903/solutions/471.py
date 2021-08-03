
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        arr = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                xi, yi = points[i]
                xj, yj = points[j]
                arr.append([i, j, abs(xi - xj) + abs(yi - yj)])
        arr.sort(key=lambda x: x[2])
        visited = set()
        res = 0
        group = []
        for i in range(len(arr)):
            u, v, d = arr[i]
            if u not in visited and v not in visited:
                visited.add(u)
                visited.add(v)
                res += d
                group.append({u, v})
            elif u in visited and v in visited:
                for idx, tmp in enumerate(group):
                    if u in tmp:
                        ui = idx
                    if v in tmp:
                        vi = idx
                if ui != vi:
                    group[ui].update(group[vi])
                    group.pop(vi)
                    res += d
            else:
                for idx, tmp in enumerate(group):
                    if u in tmp:
                        group[idx].add(v)
                        break
                    elif v in tmp:
                        group[idx].add(u)
                        break
                visited.add(u)
                visited.add(v)
                res += d

        return res
