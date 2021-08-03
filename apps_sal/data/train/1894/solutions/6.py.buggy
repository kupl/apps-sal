# Definition for singly-linked list.
 # class ListNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.next = None
 
 class Solution:
     def splitListToParts(self, root, k):
         """
         :type root: ListNode
         :type k: int
         :rtype: List[ListNode]
         """
 
         #先求长度，对长度划分
         lg=0
         p=root
         while p:
             lg+=1
             p=p.next
         #每个小序列的长度
         l=lg//k
         #分配r
         r=lg%k
         
         res=[]
         head=root
         pre=ListNode(0)
         for i in range(k):
             if head:
                 r-=1
                 res.append(head)
                 for j in range(l+(r>=0)):
                     print(22)
                     pre=head
                     head=head.next
                 pre.next=None
                 print(111)
             else:
                 res.append(None)
             
         return res
         
             
         
