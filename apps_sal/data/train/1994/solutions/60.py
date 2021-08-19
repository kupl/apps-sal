class Solution:

    def numComponents(self, head: ListNode, G: List[int]) -> int:
        tail = head
        components = 0
        connected = False
        while tail is not None:
            if tail.val in G:
                connected = True
            elif connected:
                components += 1
                connected = False
            tail = tail.next
        if connected:
            components += 1
            connected = False
        return components
