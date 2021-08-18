class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:

        if not root:
            return TreeNode(val)

        if root.val < val:
            node = TreeNode(val)
            node.left = root
            return node
        else:
            root.right = self.insertIntoMaxTree(root.right, val)

        return root
