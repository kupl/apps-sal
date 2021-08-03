# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        traverse_count = 0

        def traverse(node, max_val):
            nonlocal traverse_count
            if node.val >= max_val:
                traverse_count += 1
            max_val = max(max_val, node.val)
            if node.left:
                traverse(node.left, max_val)
            if node.right:
                traverse(node.right, max_val)
        if root:
            traverse(root, float('-inf'))
        return traverse_count
