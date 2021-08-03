# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        
        \"\"\"
        这道题分析一下其实不难，比较容易意识到需要用heap
        对于当前posi, 它应该pop heap中比它小的所有pending，然后自己进heap  
        如果最后还没出heap那就是在其后没找到比自己大的
        \"\"\"
        
        def get_length(head):
            count = 0 
            while head:
                count += 1 
                head = head.next 
            return count 
        
        length = get_length(head)
        if length == 0:
            return []
        if length == 1:
            return [0]
        
        ans = [0] * length 
        heap = []
        heapify(heap)
        index = 0
        while head:
            node = head
            head = head.next 
            while heap and heap[0][0] < node.val:
                out = heappop(heap)
                ans[out[1]] = node.val
            heappush(heap, (node.val, index))
            index += 1
        
        return ans

