class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:

        def findMaxDiff(node, max_sf, min_sf):
            if not node:
                return float('-inf')
            cur_max = max(abs(node.val - max_sf), abs(node.val - min_sf))
            max_sf, min_sf = max(max_sf, node.val), min(min_sf, node.val)
            left_max = findMaxDiff(node.left, max_sf, min_sf)
            right_max = findMaxDiff(node.right, max_sf, min_sf)
            return max(cur_max, left_max, right_max)

        return findMaxDiff(root, root.val, root.val)
