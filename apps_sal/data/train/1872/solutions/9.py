# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from collections import defaultdict


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:

        queue = deque()
        queue.append((root, 1))

        level_sums = defaultdict(int)

        while (len(queue) > 0):
            node_tuple = queue.popleft()
            curr_node = node_tuple[0]
            curr_level = node_tuple[1]
            level_sums[curr_level] += curr_node.val
            if (curr_node.left != None):
                queue.append((curr_node.left, curr_level + 1))
            if (curr_node.right != None):
                queue.append((curr_node.right, curr_level + 1))

        max_sum = root.val
        result_level = 1

        for level in list(level_sums.keys()):
            if level_sums[level] > max_sum:
                max_sum = level_sums[level]
                result_level = level

        return result_level
