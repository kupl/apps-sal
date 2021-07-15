from collections import defaultdict
class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        # scan line
        points = []
        for req in requests:
            points.append([req[0], 0]) # 0 - start
            points.append([req[1], 1]) # 1 - end
            
        points.sort(key=lambda e:(e[0], e[1]))
        freqCnt = defaultdict(int)

        pos = None
        cnt = 0
        for p in points:     
            if pos != None:
                # set right end of current interval depending on current point (start or end)
                if p[1] == 0:
                    freqCnt[cnt] += p[0] - pos
                else:
                    freqCnt[cnt] += p[0] - pos + 1
            
            if p[1] == 0:
                cnt += 1
            else:
                cnt -= 1
                
            if cnt == 0:
                pos = None
            else:
                # set left end of next interval depending on current point (start or end)
                if p[1] == 0:
                    pos = p[0]
                else:
                    pos = p[0] + 1
            
        nums.sort(reverse=True)
        result = 0
        i = 0
        for k, v in sorted(list(freqCnt.items()), reverse=True):
            result += k * sum(nums[i:i+v])
            i += v
            
        return result % (10**9+7)

