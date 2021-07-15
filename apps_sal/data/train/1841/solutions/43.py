import heapq
class Solution:
    
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        
        arr  = sorted(arr)
        length = len(arr) 
        #mid = len(arr) // 2
        median = arr[(len(arr) - 1) // 2]
        #median = (sorted_array[length // 2] + sorted_array[(length-1)//2])/2
        print()
        print(median)
        heap = []
        cnt = k
        for i in range(length):
            heapq.heappush(heap, (abs(arr[i] - median), arr[i]))
            cnt -= 1
            if cnt < 0:
                heapq.heappop(heap)
        
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])
            
        return res
                

