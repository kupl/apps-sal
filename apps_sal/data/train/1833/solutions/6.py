class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def deep(node):
            if not node:
                return 0, None
            ld = deep(node.left)
            rd = deep(node.right)

            if ld[0] > rd[0]:
                return ld[0] + 1, ld[1]
            elif rd[0] > ld[0]:
                return rd[0] + 1, rd[1]
            else:
                return ld[0] + 1, node

        return deep(root)[1]
