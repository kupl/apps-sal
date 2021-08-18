class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:

        connected_components = 0
        q = head
        G = set(G)

        while q is not None:
            if q.val in G:
                while q is not None and q.val in G:
                    q = q.__next__
                connected_components += 1
            if q is not None:
                q = q.__next__

        return connected_components
