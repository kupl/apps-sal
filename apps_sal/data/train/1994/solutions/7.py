class Solution:

    def numComponents(self, head: ListNode, G: List[int]) -> int:
        count = 0
        while head:
            if head.val in G:
                if not (head.next and head.next.val in G):
                    count += 1
            head = head.next
        return count
