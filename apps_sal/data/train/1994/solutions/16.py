# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        count=0
        node=head
        while(node):
            temp=node
            if node.val in G and getattr(node.next,'val',None) not in G:
                count+=1
            node=node.next
        return count
