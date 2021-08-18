class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        if root and root.val > val:
            root.right = self.insertIntoMaxTree(root.right, val)
            return root

        node = TreeNode(val)
        node.left = root
        return node
