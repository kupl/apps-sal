import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        h = []
        vals = {}
        cur = head
        idx = 0
        while cur:
            while len(h) > 0 and h[0][0] < cur.val:
                print(f\"{h[0]} < {cur.val}\")
                _, i = heapq.heappop(h)
                vals[i] = cur.val
            heapq.heappush(h, (cur.val, idx))
            cur = cur.next
            idx += 1
        
        res = []
        i = 0
        while head:
            res.append(vals.get(i, 0))
            head = head.next
            i += 1
        return res
        
            
        
