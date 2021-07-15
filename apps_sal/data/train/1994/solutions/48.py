# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        #s = set(G)
        
        prevIn = False
        while head:
            if head.val in G:
                if prevIn:
                    G.remove(head.val)
                else:
                    prevIn = True
            else:
                prevIn = False
            
            head = head.__next__
        
        return len(G)

