class Solution:
     def reverseBetween(self, head, m, n):
         """
         :type head: ListNode
         :type m: int
         :type n: int
         :rtype: ListNode
         """
         pre = dummy = ListNode(0)
         dummy.next = head
         num = 0
         first = last = ListNode(0)
         while head:
             num += 1
             if num == m:
                 preFirst = pre
                 first = head
             if num == n:
                 last = head
                 laLast = last.__next__
                 break
             head = head.__next__
             pre = pre.__next__
         while first != last:
             pre = first
             preFirst.next =  pre.__next__
             pre.next = last.__next__
             last.next = pre
             first = preFirst.__next__
             
         return dummy.__next__
             
             

