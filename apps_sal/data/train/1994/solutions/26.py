class Solution:

    def numComponents(self, head: ListNode, G: List[int]) -> int:
        components = 0
        G = set(G)
        while head:
            if head.val in G and (head.__next__ == None or head.next.val not in G):
                components += 1
            head = head.__next__
        return components
