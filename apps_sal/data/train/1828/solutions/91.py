class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        import collections
        import heapq
        
        c_dic = collections.Counter(barcodes)
        hp = []
        for key in c_dic:
            heapq.heappush(hp, (-c_dic[key],key))
            
        res = []
        while hp:
            collect = []
            if res:
                while hp[0][1] == res[-1]:
                    cur = heapq.heappop(hp)
                    collect.append(cur)
            
            cur = heapq.heappop(hp)   
            res.append(cur[1])
            if cur[0] != -1:
                heapq.heappush(hp, (cur[0]+1, cur[1]))
                
            for nodes in collect:
                heapq.heappush(hp, nodes)
                
        return res
