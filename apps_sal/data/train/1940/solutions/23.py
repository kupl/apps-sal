# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        
        def get_length(head):
            count = 0 
            while head:
                count += 1 
                head = head.__next__ 
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
            head = head.__next__ 
            while heap and heap[0][0] < node.val:
                out = heappop(heap)
                ans[out[1]] = node.val
            heappush(heap, (node.val, index))
            index += 1
        
        return ans

