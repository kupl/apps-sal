class Solution:

    def numComponents(self, head: ListNode, G: List[int]) -> int:
        prevIn = False
        while head:
            if head.val in G:
                if prevIn:
                    G.remove(head.val)
                else:
                    prevIn = True
            else:
                prevIn = False
            head = head.__next__
        return len(G)
