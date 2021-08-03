# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        curr = head
        i = 0
        res = []
        stack = []
        while curr:
            res.append(0)
            val = curr.val
            while stack and stack[-1][0] < val:
                v, index = stack.pop()
                res[index] = val

            stack.append((val, i))
            i = i + 1
            curr = curr.__next__
        del stack
        # print(stack)
        return res
