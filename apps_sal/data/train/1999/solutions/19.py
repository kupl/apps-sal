class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        if not head:
            return None
        node = temp = ListNode(0)
        node.next = head

        while temp:
            total = 0
            second = temp.next
            while second:
                total += second.val
                if total == 0:
                    temp.next = second.next
                second = second.next
            temp = temp.next

        return node.next
