from bisect import bisect_left

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        \"\"\"
        We only care about the lakes that receive rain multiple times
        
        Those lakes will need to, ideally, be drained prior
        
        When we see a repeat --- we need to find the first \"Dry\" after the last
        and pop it
        \"\"\"
        ans = [float('-inf') for _ in rains]
        dry = []
        tracker = {}
        for i, r in enumerate(rains):
            if r != 0:
                ans[i] = -1
                if r in tracker:
                    idx = bisect_left(dry, tracker[r]+1)
                    if idx == len(dry):
                        return []
                    else:
                        res = dry[idx]
                        ans[res] = r
                        dry.pop(idx)
                tracker[r] = i
            else:
                dry.append(i)
        for i in range(len(ans)):
            if ans[i] == float('-inf'):
                ans[i] = 1
        return ans
