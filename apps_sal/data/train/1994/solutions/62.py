# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        count = 0
        temp = 0
        s = 1
        while head:
            if head.val in G:
                temp += 1
            else:
                temp = 0
                s = 1
            head = head.next
            if temp > 0 and s == 1:
                s = 0
                count += 1
        if temp > 0 and s == 1:
            s = 0
            count += 1

        return count
