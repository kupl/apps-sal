# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        count=0
        s=set(G)
        ans=len(G)
        while head and head.__next__:
            if (head.val in G) and (head.next.val in G):
                ans-=1
            head=head.__next__
        return ans
        
              

