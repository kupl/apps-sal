# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        ##################################################################
        # solution 1, iterate through 
        components = 0
        G_set = set(G) # convert to set 
        
        while head: # iterate through
            if head.val in  G_set and ( head.__next__ == None or head.next.val  not in  G_set):
                G_set.remove(head.val)

                components += 1 
            head = head.__next__ 
            
        return components
        ##################################################################


