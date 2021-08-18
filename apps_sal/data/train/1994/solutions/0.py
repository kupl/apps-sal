class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        s = set(G)
        prev_in = False
        c = 0
        while head:
            if head.val in s:
                if not prev_in:
                    c += 1
                prev_in = True
            else:
                prev_in = False
            head = head.__next__
        return c
