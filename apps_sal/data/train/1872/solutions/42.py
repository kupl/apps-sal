# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if not root:
            return

        from collections import deque
        import sys
        queue = deque([root])
        global_value = -sys.maxsize
        level = 0
        while queue:
            level += 1
            level_value = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                level_value += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level_value > global_value:
                global_value = level_value
                global_level = level

        return global_level
