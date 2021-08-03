from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def rec(root, d, lvl):
    d[lvl] += root.val
    if root.left:
        rec(root.left, d, lvl + 1)
    if root.right:
        rec(root.right, d, lvl + 1)


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        d = defaultdict(int)
        rec(root, d, 1)
        ans = 1
        for i in d:
            if d[i] > d[ans]:
                ans = i

        return ans
