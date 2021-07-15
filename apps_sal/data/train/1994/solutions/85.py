# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        count = 0
        temp = head
        while(temp):
            if(temp.val in G):
                count = count + 1
                while(temp and temp.val in G):
                    temp = temp.__next__
            else:
                temp = temp.__next__
        return count

