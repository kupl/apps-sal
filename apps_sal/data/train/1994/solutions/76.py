# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, g: List[int]) -> int:
        g = set(g)
        n = 0
        temp = head
        while temp != None:
            n += 1
            temp = temp.next
        a = [0] * n
        i = 0
        ans = 0
        while head and i < n:
            if head.val in g:
                a[i] = 1
            i += 1
            head = head.next
        for i in range(n):
            if a[i] == 1:
                if i == 0:
                    ans += 1
                elif a[i - 1] == 0:
                    ans += 1
        return ans
