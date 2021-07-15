# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def remove_range(self, head, start_prev, stop):
        if start_prev is None:
            return stop
        else:
            start_prev.next = stop
            return head
    
    def detect_zero(self, head):
        prev = None
        stop = head
        hist = {0: None}
        acc = 0
        while stop is not None:
            acc += stop.val
            try:
                start_prev = hist[acc]
            except KeyError:
                hist[acc] = stop
                prev = stop
                stop = stop.__next__
                continue
            return True, start_prev, stop.__next__
        return False, None, None
    
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        while True:
            found, start_prev, stop = self.detect_zero(head)
            if not found:
                return head
            head = self.remove_range(head, start_prev, stop)

