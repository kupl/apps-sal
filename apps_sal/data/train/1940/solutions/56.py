# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        stk, res = [], []
        while head:
            while stk and head.val > stk[-1][1]:
                idx = stk.pop()[0]
                res[idx] = head.val
            stk.append([len(res), head.val])
            res.append(0)
            head = head.__next__
        return res
