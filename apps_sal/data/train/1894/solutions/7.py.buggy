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
         '''
         total = 0
         nums = list()
         head = root
         while head:
             total += 1
             nums.append(head.val)
             head = head.next
         
         if total%k == 0:
             size = max(total//k, 1)
             total = k * size
             res = list()
             for i in range(0, total, size):
                 tmp = nums[i: i+size]
                 if not tmp:
                     tmp = []
                 res.append(tmp)
             return res
         else:
             len1 = total%k
             len2 = k - len1
             size1 = max(math.ceil(total/k), 1)
             size2 = max(total//k, 1)
             total1 = size1 * len1
             total2 = size2 * len2
             res1 = list()
             res2 = list()
             for i in range(0, total1, size1):
                 tmp = nums[i: i+size1]
                 if not tmp:
                     tmp = []
                 res1.append(tmp)
             #print('0', total1, size1, res1)
             for i in range(total1, total1+total2, size2):
                 tmp = nums[i: i+size2]
                 if not tmp:
                     tmp = []
                 res2.append(tmp)
             #print(total1, total, size2, res2)
             return res1+res2
         '''
         total = 0
         head = root
         while head:
             total += 1
             head = head.next
         head = root
         size = total//k
         remain = total%k
         res = list()
         for i in range(k):
             tmp = list()
             for j in range(size):
                 try:
                     tmp.append(head.val)
                     head = head.next
                 except:
                     continue
             if remain > 0:
                 try:
                     tmp.append(head.val)
                     head = head.next
                 except:
                     continue
                 remain -= 1
             res.append(tmp)
         return res

