# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        max_level = -1
        max_sum = -float('inf')

        lv = 1
        lv_nodes = [root]
        while lv_nodes:
            
            if max_sum < sum([n.val for n in lv_nodes]):
                max_level = lv
                max_sum = sum([n.val for n in lv_nodes])
            lv += 1
            new_nodes = []
            for n in lv_nodes:
                if n.left:
                    new_nodes.append(n.left)
                if n.right:
                    new_nodes.append(n.right)
            lv_nodes = new_nodes
        return max_level


