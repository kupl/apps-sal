class Solution:

    def numComponents(self, head: ListNode, g: List[int]) -> int:
        count = 0
        while head:
            if head.val in g:
                if head.next and head.next.val in g:
                    head = head.next
                    continue
                count += 1
            head = head.next
        return count
