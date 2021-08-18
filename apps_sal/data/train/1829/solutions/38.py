class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def check(node, val):
            if not node:
                return 0
            if node.val >= val:
                return 1 + check(node.left, node.val) + check(node.right, node.val)
            return check(node.left, val) + check(node.right, val)
        return check(root, root.val)
