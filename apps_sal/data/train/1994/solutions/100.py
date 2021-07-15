# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        initial_c = len(G)
        
        runner = head
        # Approach 1
#         ans = []
#         conn_ll = []
#         while runner:
#             if runner.val in G:
#                 conn_ll.append(runner.val)
#             else:
#                 if conn_ll:
#                     ans.append(conn_ll[:])
#                     conn_ll = []
#             runner = runner.next
            
#         if conn_ll:
#             ans.append(conn_ll)

#         return len(ans)

        # Approach 2
        count = 0
        while runner:
            if runner.val in G and getattr(runner.next, 'val', None) not in G:
                count += 1
            runner = runner.next
        return count 
