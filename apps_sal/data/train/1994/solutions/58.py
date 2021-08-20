class Solution:

    def numComponents(self, head: ListNode, G: List[int]) -> int:
        window = False
        connected = 0
        node = head
        while node:
            if node.val in G:
                window = True
            elif window:
                connected += 1
                window = False
            node = node.__next__
        if window:
            connected += 1
        return connected
