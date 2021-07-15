# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        uniques = set(G)
        isConnected = False
        num = 0
        while head:
            if not isConnected and (head.val in uniques):
                isConnected = True
                num += 1
            if head.val not in uniques:
                isConnected = False
            head = head.__next__
        return num

