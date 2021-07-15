# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        
        count = 0
        while(head):
            if(head.val in G):
                while(head.next and head.next.val in G):
                    head = head.next
                count += 1
            head = head.next
        return count
