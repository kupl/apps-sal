# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def dfs(root):
            if root:
                vals.add(root.val)
                dfs(root.left)
                dfs(root.right)
                
        def dfs2(root, anss):
            if root:
                for a in anss:
                    v = abs(a-root.val)
                    if v in vals and v > self.ans:
                        self.ans = v
                dfs2(root.left, anss+[root.val])
                dfs2(root.right, anss+[root.val])
                
        vals = set()
        dfs(root)
        self.ans = float(\"-inf\")
        dfs2(root, [])
        return self.ans
        
