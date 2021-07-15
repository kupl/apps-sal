# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        layer = 0
        total = [0]
        
        self.dfs(root, total, layer)
        print(total)
        return total[len(total)-1]
        
    def dfs(self, node, total, layer):
        if layer > len(total) - 1:
            total.append(0)
        if not node.left and not node.right:
            total[layer] += node.val
        
        if node.left:
            self.dfs(node.left, total, layer + 1)
        if node.right:
            self.dfs(node.right, total, layer + 1)

