# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:

        count = 0
        p1, p2 = head, head

        while p2:
            if p1.val in G:
                p2 = p1.next
                p1 = p2
                if not p2 or p2.val not in G:
                    count += 1
            else:
                p1 = p2.next
                p2 = p1

        return count
