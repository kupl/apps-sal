class Solution:

    def numComponents(self, head: ListNode, g: List[int]) -> int:
        count = 0
        while head:
            if head.val in g and (head.next is None or head.next.val not in g):
                count += 1
            head = head.next
        return count
