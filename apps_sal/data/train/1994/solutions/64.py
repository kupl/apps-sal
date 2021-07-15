# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        cur = head
        con = 0
        ans = 0
        while cur:
            if cur.val not in G:
                if con != 0:
                    ans += 1
                con = 0
            else:
                con += 1
            cur = cur.next
        if con != 0:
            ans += 1
        return ans
