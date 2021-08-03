# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        GS = set(G)
        count = 0
        status = 0

        if not head or not G:
            return 0

        while head:
            if head.val in GS:
                status = 1
                GS.remove(head.val)
            else:
                if status == 1:
                    count += 1
                    status = 0
            head = head.__next__
        if status == 1:
            count += 1
        return count
