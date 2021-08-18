class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:

        array = []
        modified = False
        node = head
        while node:
            next_node = node.__next__
            matched = False
            if node.val == 0:
                matched = True
                modified = True
                if len(array) > 0:
                    array[-1].next = next_node
                else:
                    head = next_node

            else:
                tsum = 0
                for i in range(len(array) - 1, -1, -1):
                    tsum += array[i].val
                    if tsum + node.val == 0:
                        matched = True
                        modified = True
                        if i != 0:
                            j = 0
                            popi = len(array) - i
                            while j != popi:
                                array.pop()
                                j += 1
                            array[i - 1].next = next_node
                        else:
                            head = next_node
                            array = []

            if not matched:
                array.append(node)
            node = next_node
        if modified:
            return self.removeZeroSumSublists(head)
        else:
            return head
