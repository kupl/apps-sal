# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        if head is None: return 0
        s = set(G)
        cur = head
        count = 0
        
        while cur:
            seen = set()
            if cur.val not in seen and cur.val in s:
                
                while cur and cur.val not in seen and cur.val in s:
                    seen.add(cur.val)
                    cur = cur.__next__ 
                count += 1
            else:
                cur = cur.__next__ 
        return count
            

