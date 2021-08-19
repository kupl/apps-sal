# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        c = 0
        els = {}
        check = False
        for el in G:
            els[el] = True
        while head != None:
            if head.val in els:
                if not check:
                    c += 1
                    check = True
            else:
                check = False
            head = head.__next__
        return c
