
import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        if not head:
            return []

        h = []
        res = {}
        cur = head
        i = 0
        while cur:
            if len(h) == 0:
                heappush(h, (cur.val, i))
            else:
                while h and cur.val > h[0][0]:
                    val, index = heappop(h)
                    res[index] = cur.val
                heappush(h, (cur.val, i))
            i += 1
            cur = cur.next
        while h:
            val, index = h.pop()
            print(val, index)
            res[index] = 0

        return [res[index] for index in sorted([k for k in res])]
