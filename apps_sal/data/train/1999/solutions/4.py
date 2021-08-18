class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prefixSum = 0
        cur = head
        dic = {0: dummy}
        while cur:
            prefixSum += cur.val
            dic[prefixSum] = cur
            cur = cur.next
        head = dummy
        prefixSum = 0
        while head:
            prefixSum += head.val
            head.next = dic[prefixSum].next
            head = head.next
        return dummy.next
