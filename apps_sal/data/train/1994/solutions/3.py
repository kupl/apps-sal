class Solution:

    def numComponents(self, head: ListNode, G: List[int]) -> int:
        res = 0
        while head:
            if head.val in G:
                if not head.next:
                    res += 1
                elif head.next.val not in G:
                    res += 1
            head = head.next
        return res
