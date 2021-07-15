# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        count = 0
        con = False
        while head:
            if head.val in G:
                if not con:
                    con = True
                    count += 1
            else:
                if con:
                    con = False
            head = head.__next__
        return count
                
            

