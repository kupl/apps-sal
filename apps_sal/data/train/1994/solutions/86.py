# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        while(head and head.next):
            if head.val in G and head.next.val in G:
                G.remove(head.val)
            head = head.next
        return len(G)
