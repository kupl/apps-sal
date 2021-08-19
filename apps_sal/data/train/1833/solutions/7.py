class Solution:

    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:

        def helper(node, depth):
            if not node:
                return (depth, None)
            (ld, ln) = helper(node.left, depth + 1)
            (rd, rn) = helper(node.right, depth + 1)
            if ld == rd:
                return (ld, node)
            if ld > rd:
                return (ld, ln)
            if ld < rd:
                return (rd, rn)
        (depth, res) = helper(root, 0)
        return res
