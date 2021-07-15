class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        ps_start=collections.defaultdict(int)
        ps_end=collections.defaultdict(int)
        for s,e in requests:
            ps_start[s]-=1
            ps_end[e]+=1
        res=[]
        for p in ps_start:res.append([p,ps_start[p]])
        for p in ps_end:res.append([p,ps_end[p]])
        res.sort()
        
        
        freq=[[i,0] for i in range(len(nums))]
        # print(res)
        prev,count=0,0
        for p,v in res:
            if v<0:#start
                for i in range(prev,p):
                    freq[i][1]+=count
                prev=p
                count-=v
            else:
                for i in range(prev,p+1):
                    freq[i][1]+=count
                prev=p+1
                count-=v
        freq.sort(key=lambda x:x[1])
        ans=0
        k=0
        # print(freq)
        nums.sort()
        mod=1000000007
        for i,f in freq:
            ans+= (f*nums[k])%mod
            k+=1
        return ans%mod
            

