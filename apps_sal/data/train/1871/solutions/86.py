# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:

        self.max_d = 0

        def get_distance_list(node, dist_list):
            dist_list_new = []
            if not (node.left or node.right):
                return [0]
            else:
                if node.left:
                    dist_list_l = get_distance_list(node.left, dist_list)
                    diff_l = node.val - node.left.val
                    dist_list_l = [d + diff_l for d in dist_list_l]
                    dist_list_new += dist_list_l
                    dist_list_new.append(diff_l)
                if node.right:
                    dist_list_r = get_distance_list(node.right, dist_list)
                    diff_r = node.val - node.right.val
                    dist_list_r = [d + diff_r for d in dist_list_r]
                    dist_list_new += dist_list_r
                    dist_list_new.append(diff_r)
            for d in dist_list_new:
                if abs(d) > self.max_d:
                    self.max_d = abs(d)
            return dist_list_new

        get_distance_list(root, [])
        return self.max_d
