class Solution:

    def maxAncestorDiff(self, root: TreeNode) -> int:
        best = {0: -1}

        def maxmin(root, path):
            if root == None:
                return 200000
            else:
                best[0] = max(best[0], max([0] + [abs(root.val - val) for val in path]))
                maxmin(root.left, path + [root.val])
                maxmin(root.right, path + [root.val])
        maxmin(root, [])
        return best[0]
