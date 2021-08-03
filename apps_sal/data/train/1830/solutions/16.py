class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        fill = {}
        dry = []
        ans = [0] * len(rains)
        for i, v in enumerate(rains):
            if v == 0:
                dry.append(i)
                continue
            if v not in fill:
                fill[v] = i
                ans[i] = -1
            elif v in fill:
                idx = bisect.bisect_left(dry, fill[v])
                if idx == len(dry):
                    return []
                else:
                    ans[dry[idx]] = v
                    dry.pop(idx)
                fill[v] = i
                ans[i] = -1
        for i in range(len(ans)):
            if ans[i] == 0:
                ans[i] = 1
        return ans
