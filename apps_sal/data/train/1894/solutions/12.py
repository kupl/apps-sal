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
         count = 0
         node = root
         while node:
             count += 1
             node = node.next
         baseNodeLen = int(count / k)
         extraLenCount = count % k
         ans = []
         newRoot = root
         for index in range(k):
             if newRoot == None:
                 ans.append(None)
                 continue
             currentLen = baseNodeLen
             lastNode = newRoot
             if extraLenCount > 0:
                 currentLen += 1
                 extraLenCount -= 1
             for i in range(currentLen - 1):
                 lastNode = lastNode.next
             currentRoot = newRoot
             newRoot = lastNode.next
             lastNode.next = None
             ans.append(currentRoot)
         return ans
