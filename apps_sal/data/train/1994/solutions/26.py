# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        ##################################################################
        # N.B Description is pure bullshit
        # solution 1, iterate through
        components = 0
        G = set(G)  # convert to set

        while head:  # iterate through
            if head.val in G and (head.__next__ == None or head.next.val not in G):

                components += 1
            head = head.__next__

        return components
        ##################################################################
