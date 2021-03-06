class Solution:

    def numComponents(self, head: ListNode, G: List[int]) -> int:
        count = 0
        while head:
            if head.val in G:
                while head and head.val in G:
                    head = head.next
                count += 1
                if not head:
                    break
            head = head.next
        return count
