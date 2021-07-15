# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        
        ##### Using dfs and finding diff of min and max values
        self.mx=0
        path=[]
        def getpath(root):
            if not root:
                return
            path.append(root.val)
            self.mx=max(self.mx,abs(min(path)-max(path)))
            #print(path)
            getpath(root.left)
            getpath(root.right)
            path.pop()
            
        getpath(root)
        return self.mx
       
                    
                    

