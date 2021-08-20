class Solution:

    def numComponents(self, head: ListNode, G: List[int]) -> int:
        count = 0
        cur = head
        cons = False
        while cur:
            if cur.val in G:
                if not cons:
                    cons = True
                    count += 1
            else:
                cons = False
            cur = cur.next
        return count
