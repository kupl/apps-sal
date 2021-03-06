class Solution:

    def numComponents(self, head: ListNode, G: List[int]) -> int:
        c = head
        a = 0
        while c:
            if c.val in G and getattr(c.next, 'val', None) not in G:
                a = a + 1
            c = c.next
        return a
