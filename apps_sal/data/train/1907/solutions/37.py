# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        q=[(original,cloned)]
        while q:
            a,b=q.pop()
            if a.val==target.val:
                return b
            else:
                if a.left is not None:
                    q.append((a.left,b.left))
                if a.right is not None:
                    q.append((a.right,b.right))
        
        

