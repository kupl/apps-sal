# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        curr_sum = 0
        extra = ListNode(None)
        extra.next = head
        node = head
        prev = extra
        while node:
            tmp = node
            curr_sum = 0
            while tmp:
                curr_sum += tmp.val
                if curr_sum==0:
                    break
                else:
                    tmp = tmp.__next__
            # print (tmp.val, curr_sum)
            if curr_sum==0:
                if tmp:
                    prev.next = tmp.__next__
                else:
                    prev.next = None
                node = prev.__next__
            else:
                prev = node
                node = node.__next__
            
        return extra.__next__
            
   

