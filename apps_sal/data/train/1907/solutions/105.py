class Solution:

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        def search(root, val):
            if root is None:
                return None
            if root.val == val:
                return root
            return search(root.left, val) or search(root.right, val)
        if original is None:
            return None
        return search(cloned, target.val)
