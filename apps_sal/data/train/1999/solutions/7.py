# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        node, prev, rsum = head, None, 0  # tbd = sublist To Be Deleted
        rsum_map = {}
        while node:
            rsum += node.val

            if rsum_map.get(rsum):
                link = rsum_map.get(rsum)
                link.next = node.__next__
                prev, node = link, node.__next__

                # update the map
                rsum_map = {}
                x, rsum = head, 0
                while x != node:
                    rsum += x.val
                    rsum_map[rsum] = x
                    x = x.__next__
                continue

            rsum_map[rsum] = node
            if node.val == 0:
                if prev:
                    prev.next = node = node.__next__
                else:
                    head = node = node.__next__
                rsum_map.pop(0)
                continue
            elif rsum == 0:
                head = node = node.__next__
                prev = None
                rsum_map = {}
                continue

            prev = node
            node = node.__next__
        return head
