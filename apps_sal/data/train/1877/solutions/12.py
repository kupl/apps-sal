class Solution:

    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:

        def generateSumT(node, s):
            if not node:
                return (None, False)
            if not node.left and (not node.right):
                if s >= limit:
                    return (node, True)
                else:
                    return (None, False)
            isValid = False
            if node.left:
                (node.left, L) = generateSumT(node.left, s + node.left.val)
                isValid |= L
            if node.right:
                (node.right, R) = generateSumT(node.right, s + node.right.val)
                isValid |= R
            if isValid:
                return (node, True)
            else:
                return (None, False)
        (rtn, _) = generateSumT(root, root.val)
        return rtn
