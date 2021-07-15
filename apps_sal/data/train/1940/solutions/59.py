# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        vals = []
        stack = []
        node = head
        
        while node != None:
            vals.append(node.val)
            node = node.__next__
            
        if len(vals) == 1:
            return [0]
        if len(vals) == 0:
            return 0
        
        res = [0 for _ in range(len(vals))]
        
        for i,val in enumerate(vals):
            while stack:
                if vals[stack[-1]] < val:
                    pos = stack.pop()
                    res[pos] = val
                else:
                    break
                
            stack.append(i)
            
        while stack:
            pos = stack.pop()
            res[pos] = 0
        return res
        

