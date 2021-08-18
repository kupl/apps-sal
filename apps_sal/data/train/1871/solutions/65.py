class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:

        def maxDiff(root, ancestors):
            if root is None:
                return 0

            maxRightHere = 0
            for ancestor in ancestors:
                difference = abs(ancestor - root.val)
                if difference > maxRightHere:
                    maxRightHere = difference

            ancestors.append(root.val)
            maxLeft = maxDiff(root.left, ancestors)

            maxRight = maxDiff(root.right, ancestors)
            ancestors.pop()

            return max(maxRightHere, maxLeft, maxRight)

        return maxDiff(root, [])
