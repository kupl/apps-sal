# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.result = 0
        self.check_node(root, root.val)
        return self.result
        
    def check_node(self, node, max_value):
        if node.val >= max_value:
            self.result += 1
        max_value = max(max_value, node.val)
        if node.left != None:
            self.check_node(node.left, max_value)
        if node.right != None:
            self.check_node(node.right, max_value)

