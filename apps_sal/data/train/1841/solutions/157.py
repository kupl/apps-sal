import heapq

class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        n = len(arr)
        if n % 2 == 1:
            m = arr[n // 2]
        else:
            m = arr[n // 2 - 1]
        
        ans = []
        q = [(-abs(arr[i] - m), -i) for i in range(n)]
        heapq.heapify(q)
        
        for _ in range(k):
            ans.append(arr[-heapq.heappop(q)[1]])
        
        return ans
        

