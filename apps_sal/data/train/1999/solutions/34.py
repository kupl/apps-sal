class Solution:

    def deleteNodes(self, node: ListNode, num: int) -> ListNode:
        assert node != None
        assert num > 0
        dummy = ListNode(0, node)
        prev = dummy
        while node != None and num != 0:
            prev.next = node.next
            node = node.next
            num = num - 1
        assert num == 0
        return dummy.next

    def findSumZero(self, head: ListNode) -> int:
        assert head != None
        n = 1
        s = 0
        node = head
        while node != None:
            s = s + node.val
            if s == 0:
                return n
            node = node.next
            n = n + 1
        return 0

    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        prev = dummy
        node = head
        while node != None:
            n = self.findSumZero(node)
            if n > 0:
                node_next = node
                for i in range(n):
                    node_next = node_next.next
                prev.next = node_next
                node = node_next
            else:
                prev = node
                node = node.next
        return dummy.next
