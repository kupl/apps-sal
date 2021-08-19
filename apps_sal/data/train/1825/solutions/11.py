class Solution:

    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:

        def getDepth(root):
            if not root:
                return 0
            return 1 + max(getDepth(root.left), getDepth(root.right))
        maxDepth = getDepth(root)

        def helper(root, d):
            nonlocal ans, maxDepth
            if not root:
                return 0
            left = helper(root.left, d + 1)
            right = helper(root.right, d + 1)
            if left == right and left == maxDepth - d - 1:
                ans = root
            return 1 + max(left, right)
        ans = None
        helper(root, 0)
        return ans
