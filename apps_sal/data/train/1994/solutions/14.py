class Solution:

    def numComponents(self, head: ListNode, G: List[int]) -> int:
        count = 0
        prev = None
        while head:
            if head.val in G and (not prev in G):
                count += 1
            prev = head.val
            head = head.next
        return count
