class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        if barcodes is None or len(barcodes) ==0:
            return []
        
        n = len(barcodes)
        dict_t ={}
        
        for i in range(n):
            temp = barcodes[i]
            dict_t[temp] = dict_t.get(temp, 0)+1 
            
        hp =[]
        
        for key, value in dict_t.items():
            heapq.heappush(hp, (-value, key))
        
        result =[]
        
        count1 = 0 
        count2 = 0 
        while hp:
            count1, key1 = heapq.heappop(hp)
            if hp:
                count2, key2 = heapq.heappop(hp)
            
            if count1 < 0 and count2 < 0:
                result.append(key1)
                result.append(key2)
                count1 += 1 
                count2 += 1
            elif count1 <0 and count2 ==0:
                result.append(key1)
                count1 +=1 
                
            if count1 <0:
                heapq.heappush(hp, (count1, key1))
            if count2 <0:
                heapq.heappush(hp, (count2, key2))
        
        return result
