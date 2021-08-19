class Solution:

    def numComponents(self, head: ListNode, G: List[int]) -> int:
        components = 0
        G_set = set(G)
        while head:
            if head.val in G_set and (head.__next__ == None or head.next.val not in G_set):
                G_set.remove(head.val)
                components += 1
            head = head.__next__
        return components
