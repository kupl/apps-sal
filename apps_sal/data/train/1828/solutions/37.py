class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        '''
        Method
        
        
        1). Create a count the frequency
        2) use that count to create a min heap by taking the neg values of the count
        3) use the two highest count nums in the heap to change the barcode indicies
        4) at the same time, decrement said values by adding 1 and keep a check to see when the heap is empty
        5) at the end, make sure the heap is empty as there may be 1 extra value due to an odd num
        
        '''
        
        
        count = defaultdict(int)
        
        for i in barcodes:
            count[i] += 1
            
            
        heap= []
        
        for key, val in list(count.items()):
            heap.append([-val, key])
            
        heapq.heapify(heap)
        idx = 0
        
        while len(heap) > 1:
            one = heapq.heappop(heap)
            two = heapq.heappop(heap)
            
            barcodes[idx] = one[1]
            idx += 1
            barcodes[idx] = two[1]
            idx += 1
            
            one[0] += 1
            two[0] += 1
            
            
            if one[0] != 0:
                heapq.heappush(heap, one)
            if two[0] != 0:
                heapq.heappush(heap, two)
                
            
        if heap:
            barcodes[idx] = heapq.heappop(heap)[1]
            
        return barcodes
                
            


