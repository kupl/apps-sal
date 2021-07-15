# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.mx=0
        path=[]
        def getpath(root):
            if not root:
                return
            path.append(root.val)
            if len(path)>1:
                self.mx=max(self.mx,abs(min(path[:-1])-path[-1]))
                self.mx=max(self.mx,abs(max(path[:-1])-path[-1]))
                #print(path)
            getpath(root.left)
            getpath(root.right)
            path.pop()
            
        getpath(root)
        return self.mx
