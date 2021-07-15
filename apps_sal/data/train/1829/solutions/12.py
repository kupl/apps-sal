# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        self.traverse(root, root.val)
        return self.ans
    
    def traverse(self, root, so_far):
        if root:
            if root.val >= so_far:
                self.ans += 1
                so_far = root.val
            self.traverse(root.left, so_far)
            self.traverse(root.right, so_far)

