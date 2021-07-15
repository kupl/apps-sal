import heapq
class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        
        
        mymap = collections.defaultdict(int)
        n = len(nums)
        freqs = [0]*(n+1)
        for i, j in requests:
            freqs[i] += 1         
            freqs[j+1] -= 1
            
#         MADE ... prefix Sum ... algo ... to make if proper normalize ... the number of requests
#         thru indexes..
        for i in range(1, n+1):
            freqs[i] += freqs[i-1]
            
        
            
            
        
        # THIS IS TAKING o(n^2):- .... need to reduce this ... later part is amazingly fast
#         TLE -------------------------------------------------------------------------------------------      so .. we implemented above logic ... to reduce complexity

        
        # for req in requests:
        #     for ind in range(req[0], req[1]+1):
        #         mymap[ind] += 1
        
        
        
#         freqs = sorted(mymap.values(), reverse=True)
        freqs = sorted(freqs[:-1], reverse=True)
        heap = [(-n, n) for n in nums]
        
        heapq.heapify(heap)
        
        tot = 0
        for i, freq in enumerate(freqs):
            num = heapq.heappop(heap)[1]
            tot += num*freq
            tot %= (10**9 + 7)
            
        return tot % (10**9 + 7)
