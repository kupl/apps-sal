# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        curr = head
        prefix_sum = [0]
        d = {}
        d[0] = dummy
        i = 1

        while curr:
            prefix_sum.append(prefix_sum[-1] + curr.val)
            d[i] = curr
            i += 1
            curr = curr.__next__

        i = 0
        while i < len(prefix_sum):
            j = len(prefix_sum) - 1
            while i <= j:
                if prefix_sum[j] - prefix_sum[i] == 0:
                    d[i].next = d[j].__next__
                    i = j + 1
                j -= 1

        return dummy.__next__
