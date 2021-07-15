# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, lst, root):
        max_current = lst[-1][1]
        min_current = lst[-1][0]
        if root is not None:          
            current_value = root.val
            if current_value > max_current:
                max_current = current_value
            if current_value < min_current:
                min_current = current_value
            lst.append((min_current, max_current))
            return max(self.solve(lst[:], root.left), self.solve(lst[:], root.right))
        else:
            max_val =  max_current - min_current
            return max_val

    def maxAncestorDiff(self, root: TreeNode) -> int:
        lst = [(root.val, root.val)]
        return max(self.solve(lst[:], root.left), self.solve(lst[:], root.right))
