# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def kthSmallest(self, root, k):
         """
         :type root: TreeNode
         :type k: int
         :rtype: int
         """
         count=[0]
         ans=[None]
         
         def search (head):
             if not head:
                 return
             if head.left:
                 search(head.left)
             count[0] +=1
             print(k,count[0])
             if count[0]==k:
                 ans[0]=head.val
             search(head.right)
         search(root)
         return ans[0]
