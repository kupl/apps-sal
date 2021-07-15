class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        arr = []
        for a, b in requests:
            arr.append([a, -1])
            arr.append([b, 1])
        cnt = 0
        pre = 0
        arr = sorted(arr)
        
        counter = Counter()
        for e, fg in arr:
            #print(cnt, e-pre)
            if fg == -1:
                counter[cnt] += e-pre
                pre = e
                cnt += 1
            else:
                counter[cnt] += e+1-pre
                pre = e+1
                cnt -= 1

        nums = [-e for e in nums] 
        heapq.heapify(nums)
        
        ans = 0
        for k in sorted(counter.keys())[::-1]:
            cnt = counter[k]
            while cnt!=0:
                cnt -= 1
                x = -heapq.heappop(nums)
                ans += x*k
                ans %= 10**9+7
        return ans
        
                

