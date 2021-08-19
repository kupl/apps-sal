# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        curr = head
        ccCount = 0
        inCC = False
        while curr is not None:
            if curr.val in G:
                if not inCC:
                    ccCount += 1
                G.remove(curr.val)
                inCC = True
            else:
                inCC = False
            curr = curr.next
        return ccCount
