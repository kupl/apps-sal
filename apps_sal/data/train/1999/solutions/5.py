# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        dum = ListNode(next=head)
        sum_map = {0: dum}
        l = [0]
        
        while head:
            if head.val == 0:
                sum_map[l[-1]].next = head.__next__
                head = head.__next__
                continue
                
            sv = head.val + l[-1]
            
            if sv in sum_map:
                node = sum_map[sv]
                v = l.pop()
                while v != sv:
                    sum_map.pop(v, None)
                    v = l.pop()
                node.next = head.__next__
            else:
                sum_map[sv] = head
                
            l.append(sv)
            head = head.__next__
        return dum.__next__
            

