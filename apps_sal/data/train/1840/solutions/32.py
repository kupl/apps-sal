# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        def helper(root):
            stack = [[root, True, 0], [root, False, 0]]
            ans = 0
            while stack:
                root, right, length = stack.pop()
                if root:
                    ans = max(length, ans)
                    stack.append((root.right if right else root.left, not right, length +1))
                    stack.append((root.left if right else root.right, right, 1))    
            return ans
        return helper(root)
