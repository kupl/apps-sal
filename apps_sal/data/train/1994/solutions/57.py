# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        
        connected_components = 0
        q = head
        G = set(G)
    
        
        while q is not None:
            if q.val in G:
                while q is not None and q.val in G:
                    q = q.__next__
                connected_components += 1
            if q is not None:
                q = q.__next__
                
        return connected_components
    
    
#             count = 0
#         p1, p2 = head, head
#         while p2:
#             if p1.val in G:
#                 p2 = p1.next
#                 p1 = p2
#                 if not p2 or p2.val not in G:
#                     count+=1
#             else:
#                 p1 = p2.next
#                 p2 = p1
#         return count

