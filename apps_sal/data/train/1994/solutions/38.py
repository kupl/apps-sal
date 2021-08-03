# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        if not head or not G:
            return 0

        ht = {}
        for component in G:
            ht[component] = True
        if head.val in ht:
            total = 1
        else:
            total = 0
        prev = head
        while(head.next):
            head = head.next
            if head.val in ht and prev.val in ht:
                continue
            elif head.val in ht:
                total += 1
            prev = head
        return total
