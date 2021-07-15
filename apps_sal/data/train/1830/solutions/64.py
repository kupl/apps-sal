class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        idx = defaultdict(list)
        
        for i in range(n):
            if rains[i]>0:
                idx[rains[i]].append(i)
        
        nex = defaultdict(lambda: -1)
        
        for k in idx.keys():
            for i in range(len(idx[k])-1):
                nex[idx[k][i]] = idx[k][i+1]
        
        cnt = defaultdict(int)
        pq = []
        ans = []
        
        for i in range(n):
            if rains[i]>0:
                if cnt[rains[i]]==1:
                    return []
                
                cnt[rains[i]] = 1
                
                if nex[i]!=-1:
                    heappush(pq, (nex[i], rains[i]))
                    
                ans.append(-1)
            else:
                if len(pq)==0:
                    ans.append(1)
                else:
                    _, lake = heappop(pq)
                    cnt[lake] -= 1
                    ans.append(lake)
        
        return ans
