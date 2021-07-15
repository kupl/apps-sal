# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def findBottomLeftValue(self, root):
         """
         :type root: TreeNode
         :rtype: int
         """
         r=[]
         l=[]
         rorl=[]
         def record(root,level,rl):
             if not root:
                 return
             r.append(root.val)
             l.append(level)
             rorl.append(rl)
             record(root.left,level+1,rl-1)
             record(root.right,level+1,rl+1)
         record(root,0,0)
         lastlevel=max(l)
         index=[]
         for i in range(len(l)):
             if l[i]==lastlevel:
                 index.append(i)
         tmp=r[index[0]]
         rr=rorl[index[0]]
         for ind in index:
             if rorl[ind]<rr:
                 rr=rorl[ind]
                 tmp=r[ind]
         return tmp
             
             
         
