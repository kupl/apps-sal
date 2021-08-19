class Solution:

    def removeZeroSumSublists(self, H: ListNode) -> ListNode:
        (A, b) = (ListNode(0), 1)
        A.next = H
        while b:
            (s, b, D, C) = (0, 0, {0: A}, A.next)
            while C != None:
                s += C.val
                if s in D:
                    (D[s].next, b) = (C.next, 1)
                    break
                else:
                    (D[s], C) = (C, C.next)
        return A.next
