class Solution:

    def numComponents(self, head: ListNode, G: List[int]) -> int:
        count = 0
        while head:
            if head.val in G and (not head.next or head.next.val not in G):
                count += 1
            head = head.next
        return count
