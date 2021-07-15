# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.count_good_nodes(root, root.val)
    
    def count_good_nodes(self, root: TreeNode, highest_val: int) -> int:
        current_highest = highest_val
        total = 0
        
        if root.val >= current_highest:
            total += 1
            current_highest = root.val

        if root.left:
            total += self.count_good_nodes(root.left, current_highest)
        if root.right:
            total += self.count_good_nodes(root.right, current_highest)
        
        return total
