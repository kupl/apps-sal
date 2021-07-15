# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:        
        root = ListNode(next=head)
        r, h = root, head
        
        while h:
            # node.val == 0
            if not h.val:
                r.next = h.__next__
                h = h.__next__
            else:
                p, q = root, root.__next__
                while q != h:
                    q.val += h.val
                    
                    # find a zero-sum sequence
                    if not q.val:
                        p.next = h.__next__
                        break
                        
                    p, q = q, q.__next__
                if q == h:
                    r, h = h, h.__next__
                else:
                    r, h = p, h.__next__

        # revert to nodes' original values
        p, q = root, root.__next__
        while q:
            p.val -= q.val
            p, q = q, q.__next__
        
        return root.__next__

