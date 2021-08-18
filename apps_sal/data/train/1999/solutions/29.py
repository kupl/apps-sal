class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        if head == None:
            return None

        def check(node):
            if node == None:
                return None
            n = check(node.__next__)
            node.next = n
            t = node
            c = 0
            while t != None:
                c += t.val
                if c == 0:
                    return t.__next__
                t = t.__next__
            return node

        res = check(head)
        return res
