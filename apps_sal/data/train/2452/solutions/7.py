import queue
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = queue.PriorityQueue()
        for stone in stones:
            heap.put(-stone)
        
        while heap.qsize() > 1:
            num1 = heap.get()
            num2 = heap.get()
            
            heap.put(num1-num2)
            
        return -heap.get()
