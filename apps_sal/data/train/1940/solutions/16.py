# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        p = head
        stack = []
        res = []
        i = 0

        while p:
            while stack and p.val > stack[-1][0].val:
                res[stack[-1][1]] = p.val
                stack.pop()

            stack.append((p, i))

            i += 1
            p = p.next
            res.append(0)

        return res
