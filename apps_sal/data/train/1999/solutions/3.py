from collections import OrderedDict


class Solution:

    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        nodes = OrderedDict()
        curr = head
        temp = ans = ListNode(0)
        prefix = 0
        nodes[prefix] = ListNode(0)
        while curr:
            prefix += curr.val
            node = None
            while prefix in nodes:
                node = nodes.popitem()
            if node:
                nodes[prefix] = node[1]
                curr = curr.__next__
                continue
            nodes[prefix] = curr
            curr = curr.__next__
        first = True
        for node in list(nodes.values()):
            if first:
                first = False
                continue
            temp.next = ListNode(node.val)
            temp = temp.__next__
        return ans.__next__
