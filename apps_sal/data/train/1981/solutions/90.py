class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        begin = [0] * (n+1)
        end = [0] * (n+1)
        for x,y in requests :
            begin[x] += 1
            end[y+1] += 1        
        l = []
        cnt = 0
        for i in range(n) :
            cnt += begin[i] - end[i]
            l.append(cnt)
        l.sort()
        nums.sort()
        res = 0
        for i in range(n) :
            res += l[i] * nums[i]
        return res % (10**9 + 7)
                

