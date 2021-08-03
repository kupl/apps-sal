# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        queue = deque()
        result = 1
        queue.append((root, 1))
        maxsum = - sys.maxsize
        while queue:
            size = len(queue)
            level_sum = 0
            for i in range(size):
                node, level = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append((node.left, level + 1))
                if node.right:
                    queue.append((node.right, level + 1))
            if level_sum > maxsum:
                maxsum = level_sum
                result = level
        return result
