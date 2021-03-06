class Solution:

    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:

        def helper(root, val):
            if root is None:
                return TreeNode(val)
            if val > root.val:
                return TreeNode(val, root, None)
            root.right = helper(root.right, val)
            return root
        return helper(root, val)
