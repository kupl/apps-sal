# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
 	def currentmax(self,root):
 		leftval = 0
 		if root.left != None:
 			leftval = self.currentmax(root.left)
 			leftval = 0 if leftval < 0 else leftval
 		rightval = 0
 		if root.right != None:
 			rightval = self.currentmax(root.right)
 			rightval = 0 if rightval < 0 else rightval
 		currentnode = leftval + rightval + root.val
 		if self.flag == 0:
 			self.ans = currentnode
 			self.flag = 1
 		else:
 			self.ans = self.ans if self.ans > currentnode else currentnode
 		return root.val + (leftval if leftval > rightval else rightval)
 	def maxPathSum(self, root):
 		self.ans = 0
 		self.flag = 0
 		self.currentmax(root)
 		return self.ans
