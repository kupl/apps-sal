# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        window = False
        connected = 0
        node = head
        while node:
            if node.val in G:
                window = True
            else:
                if window:
                    connected += 1
                    window = False
            node = node.__next__
        if window:
            connected += 1
        return connected
