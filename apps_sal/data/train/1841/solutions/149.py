class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        heap = []
        sorted_arr = sorted(arr)
        m = sorted_arr[(len(arr)-1)//2]
        for num in arr:
            diff = abs(num - m)
            if len(heap) == k:
                heapq.heappushpop(heap, (diff, num))
            else:
                heapq.heappush(heap, (diff, num))
        return (n for d, n in heap)

