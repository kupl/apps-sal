# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        count = 0

        while head:
            if head.val in G:
                ind = G.index(head.val)
                count += 1
                head = head.__next__
                ind += 1
                while head and head.val in G:
                    head = head.__next__

            else:
                head = head.__next__
        return(count)
