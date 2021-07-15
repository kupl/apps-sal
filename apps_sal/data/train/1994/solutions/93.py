# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        count = 0
        while head:
            if head.val in G and (head.__next__ == None or head.next.val not in G):
                count += 1
            head = head.__next__
        return count

