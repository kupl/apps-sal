# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0

        stack = [root]
        parent = {root: None}
        while stack:
            p = stack.pop()
            if p.right:
                stack.append(p.right)
                parent[p.right] = p
            if p.left:
                stack.append(p.left)
                parent[p.left] = p

        ans = 0
        for nodes in parent:
            res = []
            while nodes:
                res.append(nodes.val)
                nodes = parent[nodes]
            ans = max(ans, max(res) - min(res))

        return ans
