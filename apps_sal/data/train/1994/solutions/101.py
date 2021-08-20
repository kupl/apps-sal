class Solution:

    def numComponents(self, head: ListNode, G: List[int]) -> int:
        cur = head
        N = len(G)
        while cur:
            if cur.__next__ and cur.val in G and (cur.next.val in G):
                N -= 1
            cur = cur.__next__
        return N
