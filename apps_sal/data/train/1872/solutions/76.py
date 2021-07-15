# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        q = collections.deque()
        q.append(root)
        maxlevel, level, max = 0, 0, -float('inf')
        while q:
            total = 0
            for _ in range(len(q)):
                node = q.popleft()
                total += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
            if total > max:
                max, maxlevel = total, level
        return maxlevel
