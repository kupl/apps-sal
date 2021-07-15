# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def findBottomLeftValue(self, root):
         if root==None:
             return []
         if root.left == None and root.right == None:
             return root.val
         queue = [root]
         answer = [root.val]
         while queue != []:
             temp = []
             for curr in queue:
                 if curr.left != None and curr.right != None:
                     temp.append(curr.left.val) 
                     temp.append(curr.right.val)
                 elif curr.left == None and curr.right!=None:
                     temp.append(curr.right.val)
                 elif curr.right == None and curr.left!=None:
                     temp.append(curr.left.val)
             if temp:
                 answer.append(temp)
             nt = []
             for curr in queue:
                 if curr.left != None and curr.right != None: 
                     nt.append(curr.left)
                     nt.append(curr.right)
                 elif curr.left == None and curr.right!=None:
                     nt.append(curr.right)
                 elif curr.right == None and curr.left!=None:
                     nt.append(curr.left)
             queue = nt
         if answer[-1] != None:
             return answer[-1][0]
