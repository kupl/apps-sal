class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        points.sort()

        cols = defaultdict(list)
        for p in points:
            cols[p[0]].append(p[1])

        last_x = {}
        ans = float('inf')
        for x in sorted(cols):
            for i in range(len(cols[x])):
                for j in range(i + 1, len(cols[x])):
                    if (cols[x][i], cols[x][j]) in last_x:
                        ans = min(ans, (cols[x][j] - cols[x][i]) * (x - last_x[(cols[x][i], cols[x][j])]))
                    last_x[(cols[x][i], cols[x][j])] = x

        return ans if ans < float('inf') else 0
