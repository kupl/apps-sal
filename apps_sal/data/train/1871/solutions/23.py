# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import numpy as np


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        global_max = 0

        def dfs(t):
            if t is None:
                return []

            lim_span_l = dfs(t.left)
            lim_span_r = dfs(t.right)

            nonlocal global_max

            lim_span = [t.val]
            if lim_span_l:
                global_max = max(global_max, np.max(np.abs(t.val - np.array(lim_span_l))))
                lim_span.extend(lim_span_l)

            if lim_span_r:
                global_max = max(global_max, np.max(np.abs(t.val - np.array(lim_span_r))))
                lim_span.extend(lim_span_r)

            return [min(lim_span), max(lim_span)]

        intv = dfs(root)
        return global_max
