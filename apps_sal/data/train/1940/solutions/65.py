# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        result = [] 
        stack = []
        idx = 0
        while head:
            while stack and head.val > stack[-1][0]:
                result[stack.pop()[1]] = head.val
            stack.append((head.val, idx))                            
            result.append(0)
            head = head.__next__
            idx += 1
        return result

