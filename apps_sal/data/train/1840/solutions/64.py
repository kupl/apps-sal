# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        res = collections.namedtuple('res', 'left right total')

        def dfs(root):
            if not root:
                return res(-1, -1, -1)

            left = dfs(root.left)
            right = dfs(root.right)

            return res(left.right + 1, right.left + 1, max(left.right + 1, right.left + 1, left.total, right.total))

        return dfs(root).total
