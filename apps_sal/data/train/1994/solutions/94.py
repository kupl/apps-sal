# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
    
        count=0
        i=head
        while i:
            if i.val in G:
                count+=1
                while i and i.val in G:
                    i=i.__next__
            else :i=i.__next__
        return count

