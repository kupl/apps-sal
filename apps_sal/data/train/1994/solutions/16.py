class Solution:

    def numComponents(self, head: ListNode, G: List[int]) -> int:
        count = 0
        node = head
        while node:
            temp = node
            if node.val in G and getattr(node.next, 'val', None) not in G:
                count += 1
            node = node.next
        return count
