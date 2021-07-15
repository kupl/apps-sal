# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, path, ans):
        if not root:
            return
        if path:
            ans[0] = max(ans[0], max([abs(root.val-x) for x in path]))
        path.append(root.val)
        self.helper(root.left, path.copy(), ans)
        self.helper(root.right, path.copy(), ans)

    def maxAncestorDiff(self, root: TreeNode) -> int:
        ans = [-float('inf')]
        self.helper(root, [], ans)
        return ans[0]

