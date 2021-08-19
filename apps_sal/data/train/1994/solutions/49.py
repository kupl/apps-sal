# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        s = set(G)
        ctr = 0
        currently_connected = False
        while head:
            if head.val in G:
                if not currently_connected:
                    ctr += 1
                    currently_connected = True
            else:
                currently_connected = False
            head = head.__next__
        return ctr
