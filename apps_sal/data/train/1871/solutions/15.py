

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:

        def recurse(node):
            if node is None:
                return float('inf'), float('-inf')
            else:
                left_min, left_max = recurse(node.left)
                right_min, right_max = recurse(node.right)

                current_min = min(left_min, right_min)
                current_max = max(left_max, right_max)

                val = node.val

                d = 0
                if current_min != float('inf'):
                    d = max(d, abs(current_min - val))

                if current_max != float('-inf'):
                    d = max(d, abs(current_max - val))

                self.maxDist = max(self.maxDist, d)

                return min(current_min, val), max(current_max, val)

        self.maxDist = 0
        recurse(root)
        return self.maxDist
