class Solution:

    def numComponents(self, head: ListNode, G: List[int]) -> int:
        setG = set(G)
        output = 0
        while head:
            if head.val in setG:
                output += 1
                while head and head.val in G:
                    head = head.next
            else:
                head = head.next
        return output
