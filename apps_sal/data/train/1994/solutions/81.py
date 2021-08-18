class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        count = 0
        while head:
            if head.val in G:
                count += 1
                while head and head.val in G:
                    head = head.next
            else:
                head = head.next
        return count
