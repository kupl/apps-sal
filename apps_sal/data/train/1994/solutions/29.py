class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        ans = 0
        if not head:
            return ans
        G = set(G)

        if head.val in G:
            ans += 1
            prev_con = True
        else:
            prev_con = False

        node = head.__next__
        while node:
            if node.val in G:
                if not prev_con:
                    ans += 1
                    prev_con = True
            else:
                prev_con = False
            node = node.__next__
        return ans
