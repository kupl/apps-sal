# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        ans = 0
        cnt = 0
        while head:
            if head.val in G:
                cnt = 1
            else:
                ans += cnt
                cnt = 0
            head = head.__next__

        return ans + cnt
