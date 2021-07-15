class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        ls = len(arr)
        arr.sort()
        #median = (arr[ls//2] + arr[ls//2-1]) / 2 if ls % 2 == 0 else arr[ls//2]
        median = arr[(ls-1)//2]
        print(median)
        
        res = []
        i = 0
        for num in arr:
            if i == k:
                heapq.heappush(res, (abs(num- median), num))
                heapq.heappop(res)
            else:
                heapq.heappush(res, (abs(num- median), num))
                i += 1    
        return [x[1] for x in res]

