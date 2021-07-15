# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        curr_node = head
        value_in = False
        no = 0
        while curr_node:
            if value_in:
                if not curr_node.val in G:
                    no = no + 1
                    value_in = False
            else:
                if curr_node.val in G:
                    value_in = True
                
            curr_node = curr_node.next
        if value_in:
            no = no + 1
        return no
