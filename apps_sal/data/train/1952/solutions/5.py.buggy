
 class Solution:
     def reverseBetween(self, head, m, n):
         """
         :type head: ListNode
         :type m: int
         :type n: int
         :rtype: ListNode
         """
         dummy = ListNode(0)
         dummy.next = head
         pre = dummy
         
         for i in range(m-1):
             pre = pre.next
         
         cur = pre.next
         reverse = None
         
         for i in range(n-m+1):
             next = cur.next
             cur.next = reverse
             reverse = cur
             cur = next
         
         pre.next.next = cur
         pre.next = reverse
         
         return dummy.next
