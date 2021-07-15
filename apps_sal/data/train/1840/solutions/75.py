# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        Max=[0]
        vl=set()
        vr=set()
        def path(node,l,d):
            if node == None:
                return l
            
        
            if(d==1):    #start at right
                vr.add(node)
                return path(node.left,l+1,0) 
            else:
                vl.add(node)
                return path(node.right,l+1,1)
            
        #visited=set()
        def dfs(node):
            if(node==None):
                return 
            if(node not in vl):
                Max[0]=max(Max[0],path(node,-1,0))
            if(node not in vr):
                Max[0]=max(Max[0],path(node,-1,1))
                    
            dfs(node.left)
            dfs(node.right)
        dfs(root)
            
        return Max[0]
        
        
            

