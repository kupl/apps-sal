class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        horizontal = collections.defaultdict(set)
        vertical = collections.defaultdict(set)
        for x, y in points:
            horizontal[y].add(x)
            vertical[x].add(y)
        xlist = [x for x in vertical if len(vertical[x]) > 1]
        ans = float('inf')
        for i in range(len(xlist) - 1):
            x1 = xlist[i]
            for j in range(i + 1, len(xlist)):
                x2 = xlist[j]
                cand = []
                for y in vertical[x1]:
                    if y in vertical[x2]:
                        cand.append(y)
                if len(cand) >= 2:
                    cand.sort()
                    for i in range(len(cand) - 1):
                        ans = min(ans, abs(x2 - x1) * (cand[i + 1] - cand[i]))
        return ans if ans < float('inf') else 0
