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
         #先划分长度，在填充
         le=0#处理[]空树
         p=root
         #求长度
         while p:
             le+=1
             p=p.next
         #每个小段长度
         l=le//k
         r=le%k
         
         #填充
         res=[]
         pre=ListNode(0)
         head=root
         #k个小段
         for i in range(k):
             #root存在
             if head:
                 res.append(head)
                 r-=1
                 #每个小段里填充的元素数
                 for j in range(l+(r>=0)):
                     pre=head
                     head=head.next
                 #切断
                 pre.next=None
             else:
                 res.append(None)
         return res
         
             
         
