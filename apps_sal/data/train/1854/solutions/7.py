# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def rob(self, root):
         self.dict = {}
         return self.recurse(root)
         
     def recurse(self, root):
         if root is None:
             return 0
         if root in self.dict:
             return self.dict[root]
         else:
             x = self.recurse(root.left)
             y = self.recurse(root.right)
             a = 0 if root.left is None else self.recurse(root.left.left)
             b = 0 if root.left is None else self.recurse(root.left.right)
             c = 0 if root.right is None else self.recurse(root.right.left)
             d = 0 if root.right is None else self.recurse(root.right.right)
             ans = max(root.val+a+b+c+d , x+y)
             self.dict[root] = ans
             return ans
