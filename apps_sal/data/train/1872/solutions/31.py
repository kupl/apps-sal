# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        queue = [(root, 1)]
        l_sum = []
        
        while queue:
            c_node, c_level = queue.pop(0)
            if c_node:
                while len(l_sum) < c_level:
                    l_sum.append(0)

                l_sum[c_level-1]+=c_node.val

                queue.append((c_node.left, c_level+1))
                queue.append((c_node.right, c_level+1))
            
        l_max = None
        max_i = 0
        for i in range(len(l_sum)):
            if l_max is None or l_max < l_sum[i]:
                l_max = l_sum[i]
                max_i = i
                
        return max_i+1
