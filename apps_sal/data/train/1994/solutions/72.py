class Solution:

    def numComponents(self, head: ListNode, G: List[int]) -> int:
        curr = head
        components = 0
        in_component = False
        while curr != None:
            if curr.val in G:
                in_component = True
            elif in_component:
                components += 1
                in_component = False
            curr = curr.next
        if in_component:
            components += 1
        return components
