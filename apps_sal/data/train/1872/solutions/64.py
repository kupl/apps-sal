# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

\"\"\"
Approach: Level order traversal (BFS)
- maintain a max_level_sum 
\"\"\"


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        max_level, level, ans = -float('inf'), 0, 0
        q = collections.deque()
        q.append(root)

        while q:
            level += 1
            level_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if max_level < level_sum:
                max_level, ans = level_sum, level        
        return ans
