# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        curr_node = head
        no = 0
        while curr_node:
            if curr_node.val in G:
                curr_node = curr_node.__next__
                while curr_node and (curr_node.val in G):
                    curr_node = curr_node.__next__
                no = no + 1
            else:
                curr_node = curr_node.__next__
        return no

