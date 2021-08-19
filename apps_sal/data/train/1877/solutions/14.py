class Solution:

    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:

        def remove(node, val):
            if not node:
                return val
            l = remove(node.left, node.val + val)
            r = remove(node.right, node.val + val)
            result = 0
            if node.left and node.right:
                result = max(l, r)
            elif node.left:
                result = l
            else:
                result = r
            if l < limit:
                node.left = None
            if r < limit:
                node.right = None
            return result
        val = remove(root, 0)
        return None if val < limit else root
