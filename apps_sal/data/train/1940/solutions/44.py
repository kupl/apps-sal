# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        stack = []
        
        current = head
        ret = []
        index = 0
        while current is not None:
            ret.append(0)
            while stack and current.val > stack[-1][1]:
                i, _ = stack.pop()
                ret[i] = current.val
            
            stack.append((index, current.val))
            
            index += 1
            current = current.next
            
        return ret
