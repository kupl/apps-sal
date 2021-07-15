# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        maps = defaultdict(lambda:[]); lst = []; runner = head; 
    
        while runner:
            lst.append(runner.val)
            runner = runner.__next__
        
        for i, v in enumerate(lst): maps[v].append(i)

        res = [0 for _ in range(len(lst))]; heap = []
        for i in range(len(lst)):
            while heap and lst[i] > heap[0][0]:
                pop = heapq.heappop(heap)
                res[pop[1]] = lst[i]
            heapq.heappush(heap, (lst[i], i))
        return res
        
        

