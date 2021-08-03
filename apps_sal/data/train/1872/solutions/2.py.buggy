# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        maxLevel = 1
        maxSum = float(\"-inf\")
        queue = deque()
        queue.append(root)
        level = 1
        
        while queue:
            l = len(queue)
            levelSum = 0
            
            for _ in range(l):
                node = queue.popleft()
                levelSum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if levelSum > maxSum:
                maxLevel = level
                maxSum = levelSum
            level += 1
        
        return maxLevel
