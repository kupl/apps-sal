class Solution:

    def numComponents(self, head: ListNode, G: List[int]) -> int:
        count = 0
        con = False
        while head:
            if head.val in G:
                if not con:
                    con = True
                    count += 1
            elif con:
                con = False
            head = head.__next__
        return count
