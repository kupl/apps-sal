class Solution:
     def reverseBetween(self, head, m, n):
         """
         :type head: ListNode
         :type m: int
         :type n: int
         :rtype: ListNode
         """
         if m == 1:
             m_node = head
         else:
             m_pre = head
             for i in range(m-2):
                 m_pre = m_pre.next
             m_node = m_pre.next
         a = m_node
         b = a.next
         c = a.next
         a.next = None
         for i in range(n-m):
             c = c.next
             b.next = a
             a = b
             b = c
         m_node.next = c
         if m == 1:
             return a
         else:
             m_pre.next = a
             return head
