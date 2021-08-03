# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def rob(self, root):
         """
         :type root: TreeNode
         :rtype: int
         """
         return self.robSub(root, {})
     
     def robSub(self, root, dictionary):
         if root == None:
             return 0
         if root in dictionary:
             return dictionary[root]
         value = 0
         if root.left != None:
             value += self.robSub(root.left.left, dictionary) + self.robSub(root.left.right, dictionary)
         if root.right != None:
             value += self.robSub(root.right.left, dictionary) + self.robSub(root.right.right, dictionary)
         value = max(value+root.val, self.robSub(root.left,dictionary)+self.robSub(root.right,dictionary))
         dictionary[root] = value
         return value
         
