class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        res, s = 0, set(G)
        start = False
        while head:
            if head.val in s:
                if not start:
                    res += 1
                    start = True
            else:
                if start:
                    start = False
            head = head.next
        return res
