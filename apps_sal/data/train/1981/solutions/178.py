class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        total = []
        d = dict()
        for s,e in requests:
            d[e] = 1 if e not in d else d[e]+1
            if s:
                d[s-1] = -1 if s-1 not in d else d[s-1]-1
        ld = sorted(d.items())
        dtotal = []
        for k,v in ld[::-1]:
            if not dtotal:
                dtotal.append(v)
            else:
                dtotal.insert(0,dtotal[0]+v)
        cnt = [0]*len(nums)
        j = 0
        for i in range(len(ld)):
            while j <= ld[i][0]:
                cnt[j] = dtotal[i]
                j += 1
        cnt.sort()
        nums.sort()
        ans = 0
        for i in range(len(cnt)-1,-1,-1):
            if cnt[i] == 0:
                break
            ans += cnt[i]*nums[i]
        return ans%(10**9+7)

