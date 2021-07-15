# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    node_sum = 0
    most_depth = 0
    
    def deepestLeavesSum(self, root: TreeNode) -> int:
        depth = 0
        self.generate_deepest_node_map(root, depth)
        return self.node_sum
            
    def generate_deepest_node_map(self, node, depth):
        if node:
            if node.left:
                self.generate_deepest_node_map(node.left, depth + 1)
            if node.right:
                self.generate_deepest_node_map(node.right, depth + 1)
            if not node.right and not node.left:
                if self.most_depth == depth:
                    self.most_depth = depth
                    self.node_sum += node.val
                if self.most_depth < depth:
                    self.most_depth = depth
                    self.node_sum = node.val
                
            


