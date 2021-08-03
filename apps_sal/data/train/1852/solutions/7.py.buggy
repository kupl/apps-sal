# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def clone(self,root):
         if root==None: return root
         left=self.clone(root.left)
         temp=TreeNode(self.n)
         self.n+=1
         temp.left=left
         temp.right=self.clone(root.right)
         return temp
         
     def generateTrees(self, n):
         """
         :type n: int
         :rtype: List[TreeNode]
         """
         if n==0: return []
         mapp={0:[None],1:[TreeNode(0)]}
         
         for i in range(2,n+1):
             mapp[i]=[]
             for l in range(0,i):
                 r=i-l-1
                 for treel in mapp[l]:
                     for treer in mapp[r]:
                         temp=TreeNode(0)
                         temp.left=treel
                         temp.right=treer
                         mapp[i].append(temp)
         ans=[]
         for tree in mapp[n]:
             self.n=1
             temp=self.clone(tree)
             ans.append(temp)
         return ans
                         
                         
