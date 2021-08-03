# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:

        deep_sum = 0
        depth = 0

        queue = deque()
        queue.append([root, 0])

        while queue:
            node, curr_depth = queue.popleft()

            # if leaf node
            if not node.left and not node.right:
                # if current depth is deep that depth,
                # ex: initially going till end
                if depth < curr_depth:
                    deep_sum = node.val
                    depth = curr_depth
                else:
                    # nodes existing at same depth
                    deep_sum += node.val
            else:
                if node.left:
                    queue.append([node.left, curr_depth + 1])
                if node.right:
                    queue.append([node.right, curr_depth + 1])
        return deep_sum
