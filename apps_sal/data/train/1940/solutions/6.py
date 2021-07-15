# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        stack = []
        tail = head
        res = [] 
        if not head:
            return res
        res = [None] * 10000
        idx = 0
        while tail:
            while stack and tail.val > stack[-1][0]:
                _, i = stack.pop()
                res[i] = tail.val
            if not stack or tail.val <= stack[-1][0]:
                stack.append((tail.val, idx))
            tail = tail.next
            idx += 1
        i = 0
        while i < len(stack):
            _, index = stack[i]
            res[index] = 0
            i+=1
        return res[:idx]
