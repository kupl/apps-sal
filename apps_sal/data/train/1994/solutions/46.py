# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        gset=set(G)
        count=0
        while head:
            if head.val in gset and (head.__next__ is None or head.next.val not in gset):
                count+=1
            head=head.__next__
        return count    

